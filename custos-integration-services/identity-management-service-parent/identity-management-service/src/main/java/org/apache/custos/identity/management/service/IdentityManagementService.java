/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements. See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership. The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the
 *  specific language governing permissions and limitations
 *  under the License.
 */

package org.apache.custos.identity.management.service;

import io.grpc.Status;
import io.grpc.stub.StreamObserver;
import org.apache.custos.identity.client.IdentityClient;
import org.apache.custos.identity.management.utils.Constants;
import org.apache.custos.identity.service.*;
import org.apache.custos.tenant.profile.client.async.TenantProfileClient;
import org.apache.custos.tenant.profile.service.GetTenantRequest;
import org.apache.custos.tenant.profile.service.GetTenantResponse;
import org.apache.custos.tenant.profile.service.Tenant;
import org.lognet.springboot.grpc.GRpcService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;

/**
 * The grpc service class to use for Identity management related services
 */
@GRpcService
public class IdentityManagementService extends IdentityManagementServiceGrpc.IdentityManagementServiceImplBase {

    private static final Logger LOGGER = LoggerFactory.getLogger(IdentityManagementService.class);

    @Autowired
    private IdentityClient identityClient;

    @Autowired
    private TenantProfileClient tenantProfileClient;

    @Override
    public void authenticate(AuthenticationRequest request, StreamObserver<AuthToken> responseObserver) {
        try {
            LOGGER.debug("Request received  to authenticate for " + request.getAuthRequest().getUsername());

            AuthToken authzToken = identityClient.authenticate(request.getAuthRequest());

            responseObserver.onNext(authzToken);
            responseObserver.onCompleted();

        } catch (Exception ex) {
            String msg = "Exception occurred while authentication " + ex.getMessage();
            LOGGER.error(msg);
            responseObserver.onError(ex);
        }
    }

    @Override
    public void getUser(AuthToken request, StreamObserver<User> responseObserver) {
        try {
            LOGGER.debug("Request received  for getUser");
            User user = identityClient.getUser(request);
            responseObserver.onNext(user);
            responseObserver.onCompleted();
        } catch (Exception ex) {
            String msg = "Exception occurred while fetching " + ex.getMessage();
            LOGGER.error(msg);
            responseObserver.onError(ex);
        }
    }

    @Override
    public void getUserManagementServiceAccountAccessToken(GetUserManagementSATokenRequest request, StreamObserver<AuthToken> responseObserver) {
        try {
            LOGGER.debug("Request received  to authenticate for " + request.getTenantId());

            AuthToken token = identityClient.getUserManagementSATokenRequest(request);
            responseObserver.onNext(token);
            responseObserver.onCompleted();
        } catch (Exception ex) {
            String msg = "Exception occurred while fetching service account " + ex.getMessage();
            LOGGER.error(msg);
            responseObserver.onError(ex);
        }
    }

    @Override
    public void isAuthenticated(AuthToken request, StreamObserver<IsAuthenticateResponse> responseObserver) {
        try {
            LOGGER.debug("Request received  to isAuthenticated ");
            IsAuthenticateResponse response = identityClient.isAuthenticated(request);
            responseObserver.onNext(response);
            responseObserver.onCompleted();
        } catch (Exception ex) {
            String msg = "Exception occurred while fetching authenticated status " + ex.getMessage();
            LOGGER.error(msg);
            responseObserver.onError(ex);
        }
    }

    @Override
    public void authorize(AuthorizationRequest request, StreamObserver<AuthorizationResponse> responseObserver) {
        try {
            LOGGER.debug("Request received  to authorize " + request.getTenantId());

            GetTenantRequest tenantRequest = GetTenantRequest.newBuilder().setTenantId(request.getTenantId()).build();

            GetTenantResponse tenantResponse = tenantProfileClient.getTenant(tenantRequest);

            Tenant tenant = tenantResponse.getTenant();

            if (tenant.getRedirectUrisList() == null || tenant.getRedirectUrisCount() == 0) {
                responseObserver.onError(Status.INVALID_ARGUMENT.
                        withDescription("Wrong redirect_uri").asRuntimeException());
                return;
            }

            boolean matched = false;

            for (String redireURI : tenant.getRedirectUrisList()) {
                if (request.getRedirectUri().equals(redireURI)) {
                    matched = true;
                    break;
                }
            }

            if (!matched) {
                responseObserver.onError(Status.INVALID_ARGUMENT.
                        withDescription("Wrong redirect_uri").asRuntimeException());
                return;
            }

            GetAuthorizationEndpointRequest getAuthorizationEndpointRequest = GetAuthorizationEndpointRequest
                    .newBuilder()
                    .setTenantId(request.getTenantId()).build();

            org.apache.custos.identity.service.AuthorizationResponse response =
                    identityClient.getAuthorizationEndpoint(getAuthorizationEndpointRequest);

            String endpoint = response.getAuthorizationEndpoint();


            LOGGER.info("endpoint " + endpoint);

            String loginURL = endpoint + "?" + "client_id=" + request.getClientId() + "&" + "redirect_uri="
                    + request.getRedirectUri() + "&" + "response_type="
                    + Constants.AUTHORIZATION_CODE + "&" + "scope=" + request.getScope();

            LOGGER.info("loginURL" + loginURL);

            AuthorizationResponse resp = AuthorizationResponse.newBuilder().setLoginURI(loginURL).build();

            responseObserver.onNext(resp);
            responseObserver.onCompleted();
        } catch (Exception ex) {
            String msg = "Exception occurred while formulating login uri " + ex.getMessage();
            LOGGER.error(msg);
            responseObserver.onError(ex);
        }
    }

    @Override
    public void token(GetTokenRequest request, StreamObserver<TokenResponse> responseObserver) {
        try {
            LOGGER.debug("Request received  to token endpoint " + request.getTenantId());

            LOGGER.info("Code"+ request.getCode());
            LOGGER.info("Rediret URI" + request.getRedirectUri());

            TokenResponse response = identityClient.getAccessToken(request);

            responseObserver.onNext(response);
            responseObserver.onCompleted();

        } catch (Exception ex) {
            String msg = "Exception occurred while  fetching access token " + ex.getMessage();
            LOGGER.error(msg);
            responseObserver.onError(ex);
        }
    }
}
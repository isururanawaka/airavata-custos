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

package org.apache.custos.tenant.management.interceptors;

import io.grpc.Metadata;
import org.apache.custos.credential.store.client.CredentialStoreServiceClient;
import org.apache.custos.credential.store.service.GetOwnerIdFromTokenRequest;
import org.apache.custos.credential.store.service.GetOwnerIdResponse;
import org.apache.custos.tenant.management.service.GetCredentialRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

/**
 * This talks to custos authentication and authorization services
 * and validate auth requirements of services
 */
@Component
public class AuthInterceptor {

    private static final Logger LOGGER = LoggerFactory.getLogger(AuthInterceptor.class);

    @Autowired
    private CredentialStoreServiceClient credentialStoreServiceClient;


    public <ReqT> ReqT authorize(String method, Metadata headers, ReqT msg) {

        if (method.equals("getCredentials")) {
            String tokenWithBearer = headers.get(Metadata.Key.of("authorization", Metadata.ASCII_STRING_MARSHALLER));
            String prefix = "Bearer";
            String token = tokenWithBearer.substring(prefix.length());
            String formattedToken = token.trim();
            GetOwnerIdFromTokenRequest request = GetOwnerIdFromTokenRequest
                    .newBuilder()
                    .setToken(formattedToken)
                    .build();
            GetOwnerIdResponse response = credentialStoreServiceClient.getOwnerIdFormToken(request);
            if (response != null) {
                return (ReqT) GetCredentialRequest.newBuilder().setTenantId(response.getOwnerId()).build();
            }
        }
        return msg;
    }

}
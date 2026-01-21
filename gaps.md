# Documentation Gaps Analysis

This document identifies undocumented features in both the Trails SDK and Trails API.

## Summary

| Category | Documented | Undocumented |
|----------|------------|--------------|
| SDK Exports | ~20 | 45+ |
| API Endpoints (Trails) | 13 | 9 |
| API Endpoints (Onramp) | 0 | 11 |
| Admin Endpoints | N/A | 2 (internal) |

---

# SDK Documentation Gaps Analysis

This section identifies features exported from the `0xtrails` SDK (`packages/0xtrails/src/index.ts`) that are not currently documented in the SDK documentation (`sdk/*.mdx`).

## SDK Summary

**Total undocumented SDK exports identified: 45+**

The SDK exports many utilities and functions that developers may find useful but cannot discover through the documentation.

---

## 1. Version Utilities

**Source:** `version.js`

| Export | Type | Description |
|--------|------|-------------|
| `SDK_VERSION` | `string` | Current SDK version string |
| `getVersion()` | `() => string` | Function to get SDK version |

**Use case:** Debugging, version checks, logging.

---

## 2. Intent Storage Utilities

**Source:** `intentStorage.js`

| Export | Type | Description |
|--------|------|-------------|
| `storeIntentForMonitoring` | `function` | Store intent for background monitoring |
| `getStoredIntents` | `function` | Retrieve all stored intents |
| `removeStoredIntent` | `function` | Remove a specific stored intent |
| `clearAllStoredIntents` | `function` | Clear all stored intents |

**Use case:** Managing intent persistence for recovery, monitoring pending intents across sessions.

---

## 3. Chain & RPC Utilities

**Source:** `chains.js`, `chainSwitch.js`

| Export | Type | Description |
|--------|------|-------------|
| `getRpcUrl` | `(chainId: number) => string` | Get RPC URL for a chain |
| `getChainRpcClient` | `(chainId: number) => PublicClient` | Get viem public client for chain |
| `useChainRpcClient` | `hook` | React hook for chain RPC client |
| `attemptSwitchChain` | `(params: { walletClient, desiredChainId }) => Promise<void>` | Programmatically switch wallet chain |

**Use case:** Direct blockchain interactions, chain switching before transactions.

---

## 4. Indexer Client

**Source:** `indexerClient.js`

| Export | Type | Description |
|--------|------|-------------|
| `useIndexerGatewayClient` | `hook` | Access Sequence indexer gateway client |

**Use case:** Direct indexer queries for token balances, transaction history.

---

## 5. Intent Functions (Advanced)

**Source:** `intents.js`

| Export | Type | Description |
|--------|------|-------------|
| `quoteIntent` | `function` | Get a quote for an intent (lower-level than useQuote) |
| `getIntent` | `function` | Fetch intent data by ID |

**Types:**
- `OriginCallParams`
- `TrailsFee`

**Use case:** Direct API access for quoting and intent management.

---

## 6. Intent Receipt Monitoring

**Source:** `intentReceiptMonitor.js`, `intentReceiptPoller.js`

| Export | Type | Description |
|--------|------|-------------|
| `useIntentReceiptMonitor` | `hook` | Monitor intent receipt status in real-time |
| `pollIntentReceipt` | `function` | Poll for intent receipt completion |

**Types:**
- `IntentReceiptStatus`
- `IntentReceiptPollerOptions`
- `IntentReceiptPollerCallbacks`
- `OnOriginTransactionFound`
- `OnDestinationTransactionFound`
- `OnReceiptUpdate`

**Use case:** Building custom status UIs, tracking cross-chain transaction completion.

---

## 7. Prepare Send Function

**Source:** `prepareSend.js`

| Export | Type | Description |
|--------|------|-------------|
| `prepareSend` | `function` | Prepare a send transaction (lower-level than useQuote) |

**Use case:** Server-side preparation, custom transaction flows.

---

## 8. Fund Method Type

**Source:** `transactionIntent/types.js`

| Export | Type | Description |
|--------|------|-------------|
| `FundMethod` | `type` | Type definition for funding methods |

---

## 9. Token Utilities (Additional)

**Source:** `tokens.js`

| Export | Type | Description |
|--------|------|-------------|
| `useGetTokenImageUrl` | `hook` | Get token image URL |
| `convertApiTokenInfoToToken` | `function` | Convert API token info to Token type |

**Use case:** Custom token display, working with raw API responses.

---

## 10. Balance Formatting Utilities

**Source:** `tokenBalances.js`

| Export | Type | Description |
|--------|------|-------------|
| `formatBalanceFields` | `function` | Format balance to all field variants (raw, formatted, display) |
| `formatUsdFields` | `function` | Format USD value to all field variants |
| `formatPriceFields` | `function` | Format price to all field variants |
| `formatUsdAmountFormatted` | `function` | Format USD without currency symbol |
| `formatUsdAmountLocaleDisplay` | `function` | Format USD with locale-aware formatting |

**Types:**
- `NativeTokenBalance`
- `TokenBalance`

**Use case:** Custom balance displays, locale-aware formatting.

---

## 11. Price Utilities (Additional)

**Source:** `prices.js`

| Export | Type | Description |
|--------|------|-------------|
| `getTokenPrice` | `function` | Fetch single token price |
| `useTokenPrice` | `hook` | React hook for single token price |
| `invalidateTokenPricesCache` | `function` | Invalidate price cache |
| `calcAmountUsdPrice` | `function` | Calculate USD value for token amount |
| `normalizeNumber` | `function` | Normalize number formatting |
| `formatTvl` | `function` | Format total value locked |
| `isValidNumeric` | `function` | Validate numeric string |
| `isValidInteger` | `function` | Validate integer string |

**Use case:** Price calculations, cache management, input validation.

---

## 12. Logging Utilities

**Source:** `logger.js`

| Export | Type | Description |
|--------|------|-------------|
| `logger` | `object` | SDK logger instance |
| `getMinLogLevel` | `function` | Get minimum log level |

**Use case:** Debugging, custom logging integration.

---

## 13. Onramp Client

**Source:** `onrampClient.js`, `onramp-client/index.js`

| Export | Type | Description |
|--------|------|-------------|
| `getOnrampClient` | `function` | Get onramp client instance |
| `useOnrampClient` | `hook` | React hook for onramp client |
| `TrailsOnramp` | `class/component` | Onramp functionality |

**Use case:** Fiat-to-crypto onramp integrations.

---

## 14. Refund Transaction Utilities

**Source:** `recover.js`

| Export | Type | Description |
|--------|------|-------------|
| `buildRefundTransactionWithSignature` | `function` | Build refund tx with pre-signed hash |
| `signPayload` | `function` | Sign refund payload |
| `determineRefundCall` | `function` | Determine refund call from balances |

**Types:**
- `BuildRefundTransactionWithSignatureParams`
- `UseIntentRecoverParams`
- `UseIntentRecoverReturn`

**Use case:** Custom refund flows, recovery tooling.

---

## 15. Widget Utilities

**Source:** `widget/index.tsx`, `widget/widget.tsx`, `widget/providers/*.js`

| Export | Type | Description |
|--------|------|-------------|
| `createModalController` | `function` | Create programmatic modal controller |
| `TrailsWidgetRef` | `type` | Ref type for widget imperative handle |
| `TrailsModalProvider` | `component` | Modal context provider |
| `useTrailsModal` | `hook` | Access modal context |
| `TrailsModalContextType` | `type` | Modal context type |
| `ModalSelectionParams` | `type` | Modal selection parameters |

**Use case:** Programmatic modal control, custom modal integration.

---

## 16. API Types

**Source:** `@0xtrails/api` (re-exported)

| Export | Type |
|--------|------|
| `IntentReceipt` | `type` |
| `IntentTransaction` | `type` |
| `IntentStatus` | `type` |
| `TransactionStatus` | `type` |
| `WaitIntentReceiptRequest` | `type` |
| `WaitIntentReceiptResponse` | `type` |
| `GetIntentReceiptRequest` | `type` |
| `GetIntentReceiptResponse` | `type` |
| `QuoteIntentRequest` | `type` |
| `Intent` | `type` |
| `ExecuteIntentRequest` | `type` |
| `ExecuteIntentResponse` | `type` |
| `TrailsContracts` | `type` |

**Use case:** TypeScript type safety when working with API responses.

---

## 17. Worker Exports

**Source:** `widget/workers/intentExecutionWorker.js`

| Export | Type | Description |
|--------|------|-------------|
| `IntentExecutionWorker` | `class` | Web worker for intent execution |

**Use case:** Advanced intent execution in web workers.

---

## Recommendations

### High Priority (Commonly Needed)
1. **Chain utilities** (`getRpcUrl`, `getChainRpcClient`, `attemptSwitchChain`) - Often needed for custom integrations
2. **Intent monitoring** (`useIntentReceiptMonitor`, `pollIntentReceipt`) - Essential for custom status UIs
3. **Formatting utilities** - Useful for consistent display formatting
4. **Price utilities** (`getTokenPrice`, `calcAmountUsdPrice`) - Common requirement for DeFi apps

### Medium Priority
5. **Intent storage** - Useful for session persistence
6. **Onramp client** - Important for fiat onramp integrations
7. **Widget ref and modal controller** - Needed for programmatic control

### Lower Priority
8. **Logger** - Primarily for debugging
9. **Version utilities** - Diagnostic use
10. **API types** - TypeScript developers can discover via IDE

---

## Next Steps

1. Add documentation for high-priority items to `sdk/hooks.mdx`
2. Consider creating separate documentation pages:
   - `sdk/utilities.mdx` - For formatting, validation, and helper functions
   - `sdk/advanced.mdx` - For intent monitoring, workers, and low-level APIs
   - `sdk/onramp.mdx` - For onramp integration
3. Add TypeScript examples showing type imports

---

---

# API Documentation Gaps Analysis

This section identifies API endpoints from `trails-api` (`proto/trails-api.ridl`, `proto/trails-onramp.ridl`) that are not currently documented in `api-reference/endpoints/*.mdx`.

## Summary

**Documented endpoints: 13**
**Undocumented Trails endpoints: 9**
**Undocumented Onramp endpoints: 11**
**Admin endpoints (internal, not developer-facing): 2**

---

## Documented Endpoints (Complete)

The following 13 endpoints are fully documented:

| Endpoint | Documentation |
|----------|---------------|
| `QuoteIntent` | `api-reference/endpoints/quote-intent.mdx` |
| `CommitIntent` | `api-reference/endpoints/commit-intent.mdx` |
| `ExecuteIntent` | `api-reference/endpoints/execute-intent.mdx` |
| `WaitIntentReceipt` | `api-reference/endpoints/wait-intent-receipt.mdx` |
| `GetIntentReceipt` | `api-reference/endpoints/get-intent-receipt.mdx` |
| `GetIntent` | `api-reference/endpoints/get-intent.mdx` |
| `SearchIntents` | `api-reference/endpoints/search-intents.mdx` |
| `GetIntentHistory` | `api-reference/endpoints/get-intent-history.mdx` |
| `GetChains` | `api-reference/endpoints/get-chains.mdx` |
| `GetExactInputRoutes` | `api-reference/endpoints/get-exact-input-routes.mdx` |
| `GetExactOutputRoutes` | `api-reference/endpoints/get-exact-output-routes.mdx` |
| `GetTokenList` | `api-reference/endpoints/get-token-list.mdx` |
| `GetTokenPrices` | `api-reference/endpoints/get-token-prices.mdx` |

---

## Undocumented Trails Service Endpoints

### 1. Health & Status Endpoints

| Endpoint | Description | Request | Response |
|----------|-------------|---------|----------|
| `Ping` | Health check endpoint | None | `version: string` |
| `RuntimeStatus` | Server runtime status with uptime, services health | None | `RuntimeStatus` object |
| `Clock` | Get server timestamp | None | `serverTime: timestamp` |

**Use case:** Health monitoring, debugging, service status dashboards.

---

### 2. AbortIntent

**Endpoint:** `POST /rpc/Trails/AbortIntent`

Allows users to abort an intent that has not yet been fully executed.

| Field | Type | Description |
|-------|------|-------------|
| `intentId` | `string` | ID of the intent to abort |
| `chainId` | `uint64` | Chain where the abort transaction was submitted |
| `abortTransactionHash` | `string` | Transaction hash of the user's abort transaction |

**Response:**
- `intentId: string`
- `status: IntentStatus`

**Use case:** Cancel pending intents, handle user-initiated refunds.

---

### 3. GetExchangeRate

**Endpoint:** `POST /rpc/Trails/GetExchangeRate`

Returns exchange rate from USD to a specified fiat currency.

| Field | Type | Description |
|-------|------|-------------|
| `toCurrency` | `string` | Target currency code (e.g., "EUR", "GBP") |

**Response:**
- `exchangeRate: ExchangeRate` object

**Use case:** Display prices in user's local currency, fiat conversion calculations.

---

### 4. GetCountryList

**Endpoint:** `POST /rpc/Trails/GetCountryList`

Returns list of supported countries for onramp providers.

| Field | Type | Description |
|-------|------|-------------|
| (none) | - | No parameters required |

**Response:**
- `countries: []Country`

**Use case:** Filter onramp options by user's country, show supported regions.

---

### 5. GetTrailsContracts

**Endpoint:** `POST /rpc/Trails/GetTrailsContracts`

Returns Trails contract addresses used by the Intent stack.

| Field | Type | Description |
|-------|------|-------------|
| (none) | - | No parameters required |

**Response:**
- `TrailsContracts: TrailsContracts` (contains contract addresses per chain)

**Use case:** Programmatically get contract addresses for direct contract interactions.

---

### 6. GetEarnPools

**Endpoint:** `POST /rpc/Trails/GetEarnPools`

Returns aggregated DeFi pool information from protocols like Aave and Morpho.

| Field | Type | Description |
|-------|------|-------------|
| `chainIds` | `[]uint64` | (Optional) Filter by chain IDs |
| `protocols` | `[]string` | (Optional) Filter by protocols ("aave", "morpho") |
| `minTvl` | `float64` | (Optional) Minimum TVL in USD |
| `maxApy` | `float64` | (Optional) Maximum APY percentage |

**Response:**
- `pools: []EarnPool` - Pool details with APY, TVL, etc.
- `timestamp: timestamp` - When data was fetched
- `cached: bool` - Whether response is from cache

**Use case:** Display yield opportunities, build earn/deposit features.

---

### 7. GetFiatCurrencyList

**Endpoint:** `POST /rpc/Trails/GetFiatCurrencyList`

Returns list of supported fiat currencies for display preferences.

| Field | Type | Description |
|-------|------|-------------|
| (none) | - | No parameters required |

**Response:**
- `currencies: []FiatCurrency`

**Use case:** Currency selector for price displays, user preference settings.

---

### 8. GetIntentTransactionHistory (DEPRECATED)

**Endpoint:** `POST /rpc/Trails/GetIntentTransactionHistory`

⚠️ **DEPRECATED** - Use `GetIntentHistory` instead.

---

## Undocumented TrailsOnramp Service Endpoints

The TrailsOnramp service provides fiat-to-crypto onramp functionality via Meld integration.

### 1. GetMeldServiceProviders

**Endpoint:** `POST /rpc/TrailsOnramp/GetMeldServiceProviders`

Returns available payment service providers for onramp.

| Field | Type | Description |
|-------|------|-------------|
| `countryCode` | `string` | (Optional) Filter by country |
| `serviceProviders` | `string` | (Optional) Specific providers |
| `paymentMethodType` | `string` | (Optional) Payment method filter |
| `sourceCurrencyCode` | `string` | (Optional) Fiat currency |
| `destinationCurrencyCode` | `string` | (Optional) Crypto currency |

**Response:**
- `serviceProviders: []MeldServiceProvider` with name, status, logos, URLs

---

### 2. GetMeldCountryDefaults

**Endpoint:** `POST /rpc/TrailsOnramp/GetMeldCountryDefaults`

Returns default currency and payment methods for a country.

| Field | Type | Description |
|-------|------|-------------|
| `countryCode` | `string` | Country code (e.g., "US", "GB") |

**Response:**
- `defaults: []MeldCountryDefault` with default currency and payment methods

---

### 3. GetMeldFiatCurrencies

**Endpoint:** `POST /rpc/TrailsOnramp/GetMeldFiatCurrencies`

Returns available fiat currencies for a country.

| Field | Type | Description |
|-------|------|-------------|
| `countryCode` | `string` | Country code |

**Response:**
- `fiatCurrencies: []MeldFiatCurrency` with code, name, symbol image

---

### 4. GetMeldPaymentMethods

**Endpoint:** `POST /rpc/TrailsOnramp/GetMeldPaymentMethods`

Returns payment methods available for a fiat currency.

| Field | Type | Description |
|-------|------|-------------|
| `fiatCurrency` | `string` | Fiat currency code |

**Response:**
- `paymentMethods: []MeldPaymentMethod` with method type, name, logos

---

### 5. GetMeldCryptoCurrencies

**Endpoint:** `POST /rpc/TrailsOnramp/GetMeldCryptoCurrencies`

Returns available cryptocurrencies for onramp in a country.

| Field | Type | Description |
|-------|------|-------------|
| `countryCode` | `string` | Country code |

**Response:**
- `cryptoCurrencies: []MeldCryptoCurrency` with chain info, contract addresses

---

### 6. GetMeldPurchaseLimits

**Endpoint:** `POST /rpc/TrailsOnramp/GetMeldPurchaseLimits`

Returns purchase limits for all fiat currencies.

| Field | Type | Description |
|-------|------|-------------|
| (none) | - | No parameters required |

**Response:**
- `limits: map<string, MeldCurrencyLimits>` with min/max/default amounts

---

### 7. GetMeldQuote

**Endpoint:** `POST /rpc/TrailsOnramp/GetMeldQuote`

Returns real-time quotes from multiple onramp providers.

| Field | Type | Description |
|-------|------|-------------|
| `sourceAmount` | `string` | Fiat amount to spend |
| `sourceCurrencyCode` | `string` | Fiat currency |
| `destinationCurrencyCode` | `string` | Crypto currency |
| `countryCode` | `string` | User's country |
| `walletAddress` | `string` | Destination wallet |
| `paymentMethodType` | `string` | (Optional) Payment method |

**Response:**
- Quote with fees, exchange rate, provider details

---

### 8. CreateMeldWidgetSession

**Endpoint:** `POST /rpc/TrailsOnramp/CreateMeldWidgetSession`

Creates a widget session and returns the provider URL for embedded onramp.

| Field | Type | Description |
|-------|------|-------------|
| `sessionData` | `MeldSessionData` | Wallet, amounts, provider selection |
| `sessionType` | `string` | Session type |
| `externalCustomerId` | `string` | Your customer ID |
| `externalSessionId` | `string` | Your session ID |

**Response:**
- `widgetSession` with provider URL for iframe/redirect

---

### 9. GetMeldTransaction

**Endpoint:** `POST /rpc/TrailsOnramp/GetMeldTransaction`

Returns transaction details by transaction ID.

| Field | Type | Description |
|-------|------|-------------|
| `transactionId` | `string` | Meld transaction ID |

**Response:**
- `transaction: MeldTransaction`

---

### 10. SearchMeldTransactions

**Endpoint:** `POST /rpc/TrailsOnramp/SearchMeldTransactions`

Search onramp transactions by various filters.

| Field | Type | Description |
|-------|------|-------------|
| `statuses` | `string` | (Optional) Status filter |
| `externalSessionIds` | `string` | (Optional) Your session IDs |
| `externalCustomerIds` | `string` | (Optional) Your customer IDs |
| `from` | `string` | (Optional) Start date |
| `to` | `string` | (Optional) End date |
| `limit` | `uint32` | (Optional) Max results |

**Response:**
- `transactions: MeldTransactions`

---

### 11. CreateMeldBankLinkingConnection

**Endpoint:** `POST /rpc/TrailsOnramp/CreateMeldBankLinkingConnection`

Creates a bank linking connection for ACH transfers.

| Field | Type | Description |
|-------|------|-------------|
| `externalCustomerId` | `string` | Your customer ID |
| `institutionId` | `string` | (Optional) Bank ID |
| `institutionSearchString` | `string` | (Optional) Bank search |
| `redirectUrl` | `string` | (Optional) Return URL |
| `regions` | `[]string` | (Optional) Region filter |

**Response:**
- Connection URL for bank linking flow

---

## Admin Endpoints (Internal)

The following endpoints are for internal administration and should NOT be documented for public developers:

- `AdminRequeueIntentTransaction` - Requeue failed transactions
- `AdminRebuildIntentReceiptSummary` - Rebuild receipt summaries

---

## API Error Codes

The following error codes are defined but not documented:

| Code | Name | Description | HTTP Status |
|------|------|-------------|-------------|
| 2000 | `InvalidArgument` | Invalid argument | 400 |
| 2001 | `Unexpected` | Unexpected server error | 500 |
| 2002 | `Unavailable` | Unavailable resource | 400 |
| 2003 | `QueryFailed` | Query failed | 400 |
| 2004 | `IntentStatus` | Invalid intent status | 422 |
| 8000 | `NotFound` | Resource not found | 400 |
| 8008 | `UnsupportedNetwork` | Unsupported network | 422 |
| 8009 | `ClientOutdated` | Client is outdated | 422 |
| 7000 | `IntentsSkipped` | Intent not needed for this transaction | 400 |
| 7001 | `QuoteExpired` | Intent quote has expired | 400 |
| 9000 | `IntentsDisabled` | Intents service unavailable | 400 |

---

## Recommendations

### High Priority (Developer-facing)
1. **AbortIntent** - Critical for error handling and user control
2. **GetTrailsContracts** - Essential for direct contract integrations
3. **GetEarnPools** - Important for DeFi/yield features
4. **Error codes** - Add to `api-reference/introduction.mdx`

### Medium Priority
5. **GetExchangeRate** - Useful for multi-currency displays
6. **GetFiatCurrencyList** - Supports currency preferences
7. **GetCountryList** - Needed for onramp country selection

### Consider Documenting (Onramp)
8. **TrailsOnramp service** - If onramp is a public feature, create `api-reference/onramp/*.mdx` documentation for all 11 Meld endpoints

### Lower Priority
9. **Ping/RuntimeStatus/Clock** - Primarily for debugging/monitoring
10. **GetIntentTransactionHistory** - Deprecated, point to GetIntentHistory

---

## Next Steps

1. Add `AbortIntent` documentation to `api-reference/endpoints/`
2. Add `GetTrailsContracts` documentation
3. Add `GetEarnPools` documentation for DeFi features
4. Update `api-reference/introduction.mdx` with:
   - Error codes table
   - Rate limiting information (if applicable)
5. If onramp is public, create onramp documentation section

---

*Generated on: 2026-01-21*
*Analyzed API version: trails-api/proto/trails-api.ridl, trails-onramp.ridl*

---

*SDK Analysis generated on: 2026-01-21*
*Analyzed SDK version: packages/0xtrails/src/index.ts*

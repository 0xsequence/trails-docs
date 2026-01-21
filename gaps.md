# SDK Documentation Gaps Analysis

This document identifies features exported from the `0xtrails` SDK (`packages/0xtrails/src/index.ts`) that are not currently documented in the SDK documentation (`sdk/*.mdx`).

## Summary

**Total undocumented exports identified: 45+**

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

*Generated on: 2026-01-21*
*Analyzed SDK version: packages/0xtrails/src/index.ts*

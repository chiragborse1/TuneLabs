// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026-present the TuneLabs AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

// Internal TuneLabs API header; direct Hugging Face calls use Authorization.

export const HUB_HF_TOKEN_HEADER = "X-TuneLabs-HF-Token";

export function hubTokenHeader(
  token?: string | null,
): Record<string, string> {
  return token ? { [HUB_HF_TOKEN_HEADER]: token } : {};
}

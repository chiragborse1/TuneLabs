// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026-present the TuneLabs AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

export function normalizeNonEmptyName(
  value: string,
  fallback = "Unnamed",
): string {
  const trimmed = value.trim();
  return trimmed.length > 0 ? trimmed : fallback;
}


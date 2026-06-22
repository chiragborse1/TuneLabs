// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026-present the TuneLabs AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

const DEFAULT_LOCALE = "en" as const;
type Locale = typeof DEFAULT_LOCALE;

export function initializeLocale(): void {
  if (typeof document !== "undefined") {
    document.documentElement.lang = DEFAULT_LOCALE;
  }
}

export function getLocale(): Locale {
  return DEFAULT_LOCALE;
}

export function useLocale(): Locale {
  return DEFAULT_LOCALE;
}

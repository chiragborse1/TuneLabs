// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026-present the TuneLabs AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

import { en } from "./locales/en";
import type { InterpolationValues, MessageKey } from "./types";

export type TranslationKey = MessageKey<typeof en>;

const PLACEHOLDER_PATTERN = /\{([a-zA-Z0-9_]+)\}/g;

function readMessage(tree: unknown, key: string): string | undefined {
  let cursor = tree;
  for (const segment of key.split(".")) {
    if (
      cursor === null ||
      typeof cursor !== "object" ||
      !Object.prototype.hasOwnProperty.call(cursor, segment)
    ) {
      return undefined;
    }
    cursor = (cursor as Record<string, unknown>)[segment];
  }
  return typeof cursor === "string" ? cursor : undefined;
}

function interpolate(
  template: string,
  values: InterpolationValues | undefined,
): string {
  if (!values) return template;

  return template.replace(PLACEHOLDER_PATTERN, (match, name: string) => {
    if (!Object.prototype.hasOwnProperty.call(values, name)) return match;
    const value = values[name];
    return value === null || value === undefined ? "" : String(value);
  });
}

function warnMissingEnglishMessage(key: string): void {
  if (import.meta.env.DEV) {
    console.warn(`[i18n] Missing English translation for key "${key}".`);
  }
}

export function translate(
  key: TranslationKey,
  values?: InterpolationValues,
): string {
  const localized = readMessage(en, key);

  if (localized === undefined) {
    warnMissingEnglishMessage(key);
    return key;
  }

  return interpolate(localized, values);
}

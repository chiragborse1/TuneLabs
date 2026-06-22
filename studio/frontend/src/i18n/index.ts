// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026-present the TuneLabs AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

import { translate } from "./messages";
import type { InterpolationValues } from "./types";
import type { TranslationKey } from "./messages";

export {
  getLocale,
  initializeLocale,
  useLocale,
} from "./locale-store";
export {
  translate,
} from "./messages";
export type { TranslationKey } from "./messages";
export type {
  DeepPartialMessageTree,
  InterpolationValues,
  MessageKey,
  MessageTree,
} from "./types";

export function useT(): (
  key: TranslationKey,
  values?: InterpolationValues,
) => string {
  return (key: TranslationKey, values?: InterpolationValues) =>
    translate(key, values);
}

// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026-present the TuneLabs AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

import type { TransportMode } from "./constants";

export interface TransportConflictInfo {
  previous: TransportMode;
  next: TransportMode;
  resumable: boolean;
}

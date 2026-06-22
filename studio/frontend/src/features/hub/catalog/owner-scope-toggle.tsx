// SPDX-License-Identifier: AGPL-3.0-only
// Copyright 2026-present the TuneLabs AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

import { HubOptionMenu } from "./hub-option-menu";

export type OwnerScope = "tunelabs" | "all";

const OPTIONS: { value: OwnerScope; label: string }[] = [
  { value: "tunelabs", label: "TuneLabs" },
  { value: "all", label: "All" },
];

/**
 * "TuneLabs / All" publisher scope as a compact dropdown pill beside the
 * view-mode tabs. Only shown while browsing a model list, never on the hub feed.
 */
export function OwnerScopeToggle({
  value,
  onChange,
}: {
  value: OwnerScope;
  onChange: (value: OwnerScope) => void;
}) {
  return (
    <HubOptionMenu<OwnerScope>
      value={value}
      options={OPTIONS}
      onValueChange={onChange}
      ariaLabel="Publisher scope"
      align="end"
      className="h-8 text-[11.5px]"
    />
  );
}

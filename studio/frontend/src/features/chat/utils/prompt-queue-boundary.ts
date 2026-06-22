export const PROMPT_QUEUE_STOP_EVENT = "tunelabs:prompt-queue-stop";

export function requestPromptQueueStop() {
  if (typeof window === "undefined") {
    return;
  }
  window.dispatchEvent(new Event(PROMPT_QUEUE_STOP_EVENT));
}

import { writable } from 'svelte/store';

export const formOpen = writable(false);
export const analysisOpen = writable(false)
export const caseId = writable(null);
export const title = writable('')

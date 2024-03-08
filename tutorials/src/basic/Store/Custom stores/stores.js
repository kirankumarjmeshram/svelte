import { writable } from 'svelte/store';

function createCount() {
	const { subscribe, set, update } = writable(0);
    // custom stores
	return {
		subscribe,
		increment: ()=> update((e) => e + 1),
		decrement: ()=> update((e) => e - 1),
		reset: () => set(0)
	};
}

export const count = createCount();

import { readable } from 'svelte/store';

export const time = readable(new Date(), function start(set) {
	const interval = setInterval(()=>{
		set(new Date());
	},1000);

	return function stop() {
		// teardown code goes here
		clearInterval(interval)
	};
});

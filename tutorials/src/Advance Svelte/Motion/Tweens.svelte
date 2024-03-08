
<!-- The full set of options available to tweened:

delay — milliseconds before the tween starts
duration — either the duration of the tween in milliseconds, or a (from, to) => milliseconds function allowing you to (e.g.) 
specify longer tweens for larger changes in value
easing — a p => t function
interpolate — a custom (from, to) => t => value function for interpolating between arbitrary values. By default, 
Svelte will interpolate between numbers, dates, and identically-shaped arrays and objects (as long as they only contain 
numbers and dates or other valid arrays and objects). If you want to interpolate (for example) colour strings or transformation 
matrices, supply a custom interpolator
You can also pass these options to progress.set and progress.update as a second argument, in which case they will 
override the defaults. The set and update methods both return a promise that resolves when the tween completes. -->


<script>
	// import { writable } from 'svelte/store';
	import {tweened} from 'svelte/motion';
	import {cubicOut} from 'svelte/easing';

	// const progress = writable(0);
	// const progress = tweened(0);
	const progress = tweened(0,{
		duration: 400,
		easing:cubicOut
	});
</script>

<progress value={$progress} />

<button on:click={() => progress.set(0)}>
	0%
</button>

<button on:click={() => progress.set(0.25)}>
	25%
</button>

<button on:click={() => progress.set(0.5)}>
	50%
</button>

<button on:click={() => progress.set(0.75)}>
	75%
</button>

<button on:click={() => progress.set(1)}>
	100%
</button>

<style>
	progress {
		display: block;
		width: 100%;
	}
</style>

<script>
	import {createEventDispatcher } from 'svelte'
	function sayHello() {
		dispatch('my_message', {
			text: 'Hello!'
		});
	}
	const dispatch = createEventDispatcher();
</script>

<button on:click={sayHello}>
	Click to say hello
</button>

<script>
    import Inner from "./Inner.svelte";
    // import { createEventDispatcher } from 'svelte';
	// const dispatch = createEventDispatcher();
	// function forward(event){
	// 	dispatch('message',event.datail);
	// }
</script>
<Inner on:message />
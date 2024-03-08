<!-- Any name beginning with $ is assumed to refer to a store value. It's effectively a reserved character — Svelte will 
    prevent you from declaring your own variables with a $ prefix. -->

<script>
    // import { onDestroy } from 'svelte';
    import {count} from './stores';
    import Increment from './Increment.svelte';
    import Decrement from './Decrement.svelte';
    import Res from './Resetter.svelte'

	// let count_value;

	// const unsubscribe = count.subscribe(value =>{
	// 	count_value = value;
	// })

	// onDestroy(unsubscribe);
</script>
<!-- <h1>The count is {count_val}</h1> -->
<h1>The count is {$count}</h1>
<Increment/>
<Decrement/>
<Res/>
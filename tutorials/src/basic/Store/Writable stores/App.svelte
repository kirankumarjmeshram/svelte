<script>
    import {count} from './stores';
    import Increment from './Increment.svelte';
    import Decrement from './Decrement.svelte';
    import Res from './Resetter.svelte'

    let count_val ;
    count.subscribe((n)=>{
        count_val = n;
    })
</script>
<h1>The count is {count_val}</h1>
<Increment/>
<Decrement/>
<Res/>
<script>
    import {count} from './stores';

    function increament(){
        count.update((n)=>n+1);
    }
</script>

<button on:click={increament}>
    +
</button>
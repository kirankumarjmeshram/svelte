<script>
    import Spring from "./Motion/Spring.svelte";
import Tweens from "./Motion/Tweens.svelte";
  import CustomCssTransation from "./transitions/CustomCssTransation.svelte";
  import CustomJsTransaction from "./transitions/CustomJSTransaction.svelte";
  import DifferedTransaction from "./transitions/Differed Transaction/DifferedTransaction.svelte";
  import GlobalTransaction from "./transitions/GlobalTransaction.svelte";
  import InAndOut from "./transitions/InAndOut.svelte";
  import KeyBlock from "./transitions/KeyBlock/KeyBlock.svelte";
  import TransitionDirective from "./transitions/TransitionDirective.svelte";
  import TransitionEvents from "./transitions/TransitionEvents.svelte";
</script>
<h1><b>ADVANCE SVELTE</b></h1>
<h2>Tweens</h2>
<Tweens/>
<h2>Spring</h2>
<Spring/>
<h2>The Transaction Directive</h2>
<TransitionDirective/>
<h2>In and Out</h2>
<InAndOut/>
<h2>Custom CSS Transation</h2>
<CustomCssTransation />
<h2>Custom JS Transaction</h2>
<CustomJsTransaction/>
<h2>Transition Events</h2>
<TransitionEvents/>
<h2>Global Transaction</h2>
<GlobalTransaction/>
<h2>Key Block</h2>
<KeyBlock/>
<h2>Differed Transaction</h2>
<DifferedTransaction/>
<script>
    import AddingParameter from "./Actions/AddingParameter.svelte";
// import Usedirective from "./Actions/The Use Directive/Usedirective.svelte";
  // import BindingToComponentInstance from "./Advance Binding/Binding to Component Instance/BindingToComponentInstance.svelte";
  import ComponentBinding from "./Advance Binding/Component binding/ComponentBinding.svelte";
  import ContentEditableBinding from "./Advance Binding/ContentEditableBinding.svelte";
  import Dimensions from "./Advance Binding/Dimensions.svelte";
  import EachBlockBinding from "./Advance Binding/EachBlockBinding.svelte";
  import MediaElement from "./Advance Binding/Media Element/MediaElement.svelte";
  // import This from "./Advance Binding/This/This.svelte";
import AnimateDirective from "./Animation/AnimateDirective.svelte";
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
<h2>Animation "animate directives"</h2>
<AnimateDirective/>
<h1>Actions</h1>
<h2>(Canvas) Use Directives</h2>
<!-- <Usedirective/> -->
<h2>Adding Parameters</h2>
<AddingParameter/>

<h1>ADVANCE BINDING</h1>
<h2>Content Editable Binding</h2>
<ContentEditableBinding/>
<h2>Each block Binding</h2>
<EachBlockBinding/>
<h2>Media Element</h2>
<MediaElement/>
<h2>Dimensions</h2>
<Dimensions/>
<h2>This</h2>
<!-- <This/> -->
<h2>Component Binding</h2>
<ComponentBinding/>
<h2>Binding To The Component Instance</h2>
<!-- <BindingToComponentInstance/> -->

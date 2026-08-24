<template>
    <div>
        <div class="bg-slate-800">
            <Comheader/>
        </div>
        <div class="mb-5">
            <ComFilterSection/>
        </div>
          
        <div class="max-width">
           <ComImageSlideSection />

            <div class="mt-4 mb-4">
                <ComCardInfoSection />
            </div>

            <div>
                <ComHotPromotion />
            </div>
            
        </div>
        <div class="bg-slate-800">
            <Comfooter/>
        </div>
    </div>
</template>

<script setup>
    import { ref } from 'vue';
    import Comheader from "../CustomerScreen/components/Comheader.vue"
    import Comfooter from "../CustomerScreen/components/Comfooter.vue"
    import ComFilterSection from "../CustomerScreen/components/ComFilterSection.vue"
    import ComCardInfoSection from "../CustomerScreen/components/ComCardInfoSection.vue"
    import ComImageSlideSection from "../CustomerScreen/components/ComImageSlideSection.vue"

    import ComHotPromotion from "../CustomerScreen/components/ComHotPromotion.vue"
</script>
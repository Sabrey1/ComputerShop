<template>
    <div class="min-h-screen flex flex-col">
        <div class="bg-slate-800">
            <Comheader/>
        </div>
        <main class="flex-1">
            <div class="mb-5">
                <ComFilterSection/>
            </div>
            
            <div class="max-width">
            <ComImageSlideSection />

                <div class="mt-8 mb-4" style="margin-top: 50px; margin-bottom: 50px">
                    <ComCardInfoSection />
                </div>

                <div class="mb-5">
                    <ComHotPromotion />
                </div>
                
            </div>
        </main>
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

<template>
    <div class="max-width text-white flex flex-col justify-center" style="height: 200px;">
        <p class="text-4xl font-bold">Master <span class="text-red-500">Tech</span></p>
        <div class="flex items-center gap-2 mt-3 mb-3">
            <Phone color="red" />
            <p>010 445 201 / 089 786 502</p>
        </div>
        <div class="flex items-center gap-2">
            <MapMarker color="red" />
            <p>ទីតាំង: ខាងក្រោយពេទ្យលោកសង្ឈ ផ្លូវ​ 146 ផ្ទះលេខ229A សង្កាត់ទឹកល្អក 2 រាជធានីភ្នុំពេញ​ Cambodia</p>
        </div>
    </div>
</template>

<script setup>
    import Phone from '@primeicons/vue/phone';
    import MapMarker from '@primeicons/vue/map-marker';
</script>
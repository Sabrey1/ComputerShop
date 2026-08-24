<template>
    <div class="text-white max-width p-2">
        <div class="flex gap-4 mb-4 items-center">
            <div class="flex items-center gap-2">
                <Phone color="red" />
                <p>010 445 201 / 089 786 502</p>
            </div>
            <div class="flex items-center gap-2">
                <MapMarker color="red" />
                <p>ទីតាំង: ខាងក្រោយពេទ្យលោកសង្ឈ ផ្លូវ​ 146 ផ្ទះលេខ229A សង្កាត់ទឹកល្អក 2 រាជធានីភ្នុំពេញ​ Cambodia</p>
            </div>
        </div>

        <div class="flex gap-5 items-center mb-2">
            <p>Master Computer</p>
            <IconField class="search-box">
                <InputIcon class="pi pi-search" />
                <InputText   
                    placeholder="Search..."
                />
            </IconField>
        </div>
        
    </div>
</template>

<script setup>
    import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import Phone from '@primeicons/vue/phone';
import MapMarker from '@primeicons/vue/map-marker';
</script>

<style scoped>
.search-box,
.search-box .p-inputtext {
    width: 70%;
    border-radius: 9999px;
}</style>
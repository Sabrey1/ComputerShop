<template>
    <div class="w-full">
        <div class="p-4" style="justify-content: end; display: flex">
            <Button label="New Image Slide" class="" />
        </div>
        <DataTable :value="imageSlide" tableStyle="min-width: 50rem">
            <Column field="title" header="Title" />
            <Column field="sort_order" header="Sort Order" />
            <Column field="enable" header="Enable" />
            <Column header="Action">
                <template #body="slotProps">
                    <Button icon="pi pi-pencil" class="p-button-rounded p-button-success mr-2" />
                    <Button icon="pi pi-trash" class="p-button-rounded p-button-warning" />
                </template>
            </Column>
        </DataTable>
    </div>
</template>

<script setup>
import { ref,onMounted } from "vue";

import { useImageSlide } from "../../composable/useImageSlide.js"
const { getImageSlide,
        imageSlide } = useImageSlide()

onMounted(() => {
    getImageSlide()
})

</script>
<template>
    <div class="w-full">
        <DataTable :value="brands" tableStyle="min-width: 50rem"> 
            <Column field="name" header="Name" />
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
import { onMounted, ref } from "vue";

import { useBrand } from "../../composable/useBrand.js"
const { brands, getBrand } = useBrand()

onMounted(() => {
    getBrand()
})


</script>
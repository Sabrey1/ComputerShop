<template>
    <div class="w-full">
        <DataTable :value="categories" tableStyle="min-width: 50rem">
            <Column field="name" header="Name" />
            <Column field="description" header="Description" />
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

import { useCategory } from "../../composable/useCategory.js"
const { categories, getCategory } = useCategory()

onMounted(() => {
    getCategory()
})

</script>
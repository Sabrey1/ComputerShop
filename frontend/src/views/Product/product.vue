<template>
    <div class="w-full">
        <div class="p-4" style="justify-content: end; display: flex">
            <Button label="New Product"/>
        </div>

        <DataTable :value="products" tableStyle="min-width: 50rem"> 
            <Column field="name" header="Name" />
            <Column field="category" header="Category">
                <template #body="slotProps">
                    {{ slotProps.data.category?.name || '-' }}
                </template>
            </Column>
          
            <Column field="selling_price" header="Sale Price"></Column>
            <Column field="stock_quantity" header="Quantity"></Column>
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
import { ref, onMounted } from "vue";

import { useProduct } from "../../composable/useProduct.js"
const { products, getProduct } = useProduct()

onMounted(() => {
    getProduct()
})

</script>
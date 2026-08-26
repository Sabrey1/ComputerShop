<template>
    <div class="w-full">
        <div class="p-4" style="justify-content: end; display: flex">
            <Button label="New Customer" class="" />
        </div>
        <DataTable :value="customers" tableStyle="min-width: 50rem">
            <Column field="name" header="Name" />
            <Column field="phone" header="Phone Number" />
            <Column field="address" header="Address" />
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

import { useCustomer } from "../../composable/userCustomer.js"
const { customers, getCustomer } = useCustomer()

onMounted(() => {
    getCustomer()
})

</script>
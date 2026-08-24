<template>
    <div class="w-full">
        <DataTable :value="suppliers" tableStyle="min-width: 50rem">
            <Column field="name" header="Name" />
            <Column field="contact_person" header="Contact Person" />
            <Column field="phone" header="Phone Number" />
            <Column field="email" header="Email" />
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

import { useSupplier } from "../../composable/useSupplier.js"
const { suppliers, getSupplier } = useSupplier()

onMounted(() => {
    getSupplier()
})

</script>
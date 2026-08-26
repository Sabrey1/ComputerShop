<template>
    <div class="w-full">
        <div class="p-4" style="justify-content: end; display: flex">
            <Button label="New Bussiness Info" class="" />
        </div>
        <DataTable :value="businessInfo" tableStyle="min-width: 50rem"> 
            <Column field="bussiness_name" header="Bussiness Name" />
            <Column field="phone_number_1" header="Phone Number" />
            <Column field="phone_number_2" header="Phone Number 1" />
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

import { useBusinessInfo } from "../../composable/useBusinessInfo.js"
const { getBusinessInfo,
        businessInfo } = useBusinessInfo()

onMounted(() => {
    getBusinessInfo()
})


</script>
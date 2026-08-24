<template>
    <div class="flex gap-4 bg-white w-full">
        <div class="card">
            <Truck color="green" :size="40" class="icon" />
            <h1 class="mt-2">ដឹកជញ្ជូន២៥ខេត្តក្រុង</h1>
        </div>
        <div class="card"> 
            <MoneyBill color="green" :size="40" class="icon" />
            <h1 class="mt-2">តម្លៃពិសេសជាងគេក្នុងទីក្រុង</h1>
        </div>
        <div class="card">
            <Shield color="green" :size="40" class="icon" />
            <h1 class="mt-2">ការធានាពីហាងនិងក្រុមហ៊ុន</h1>
        </div>
        <div class="card">
            
            <Headphones color="green" :size="40" class="icon" />
            <h1 class="mt-2">ជំនួយតាមអ៊ីនធឺណិត</h1>
        </div>
    </div>
</template>

<script setup>
import Truck from '@primeicons/vue/truck';
import MoneyBill from '@primeicons/vue/money-bill';
import Shield from '@primeicons/vue/shield';
import Headphones from '@primeicons/vue/headphones';
</script>

<style scoped>
.card{
    flex:1;
    box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px;
    padding: 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.card svg {
    width: 60px !important;
    height: 60px !important;
    flex-shrink: 0;
}
.icon{
    border: 1px solid green;
    border-radius: 50%;
    padding: 10px;
}
 
</style>
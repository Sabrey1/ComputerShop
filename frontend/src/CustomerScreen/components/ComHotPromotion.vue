<template>
    <div>
        <div class="text-center">
            <h1 class="text-black text-3xl font-bold mb-2">Hot Promotion</h1>
            <div class="accent-divider mb-5">
                <span class="accent-divider__highlight"></span>
            </div>
            <slideBreak/>
        </div>
        
    </div>
</template>

<script setup>
import slideBreak from "../../components/slideBreak.vue"
</script>

<style scoped>
.accent-divider {
  position: relative;
  width: 100%;
  height: 1px;
  background-color: #e0e0e0; /* light gray line */
}

.accent-divider__highlight {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 240px;      /* length of the red segment */
  height: 2px;        /* slightly thicker than the base line */
  background-color: #b91c1c; /* red */
}
</style>
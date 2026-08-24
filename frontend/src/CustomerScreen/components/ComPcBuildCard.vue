<template>
  <div class="card">
    <div class="image-block">
        <img :src="pcImage" alt="PC" class="image" />


        <div class="text">
            <p class="title">
                PC Builder
            </p>
            <p class="subtitle">
                Choose your favorite components
            </p>
            <Button label="Build Now" />
        </div>
    </div>
    
  </div>
</template>

<script setup>
    import pcImage from "../../assets/image/Computer/pc.png";
</script>

<style scoped>
    
    .image-block{
        position: relative;
        width: 100%;
        height: 300px;
        overflow: hidden;
        border-radius: 10px;
    }
    .image{
        height: 300px;
    }
    .text {
        position: absolute;
        top: 75%;
        left: 25px;
        transform: translateY(-50%);
    }

    .title {
        font-size: 24px;
        font-weight: 600;
 
        color: #fff;
    }
    .subtitle {
        font-size: 16px;
        margin-bottom: 10px;
        color: #fff;
    }
</style>
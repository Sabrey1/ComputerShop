<template>
  <div class="app-layout">
    <div
      v-if="showSidebar && visible && isMobile"
      class="sidebar-backdrop"
      @click="closeSidebar"
    ></div>

    <aside
      v-if="showSidebar"
      class="sidebar"
      :class="{
        'sidebar-open': visible,
        'sidebar-closed': !visible
      }"
    >

      <div class="sidebar-header">
        <div class="logo">
          Ecommerce
        </div>
      </div>

      <nav class="sidebar-menu">
        <RouterLink
          to="/admin/dashboard"
          class="menu-item"
          @click="onLinkClick"
        >
          <i class="pi pi-box"></i>

          <span class="khmer-text">
            Dashboard
          </span>
        </RouterLink>

        <RouterLink
          to="/admin/category"
          class="menu-item"
          @click="onLinkClick"
        >
          <i class="pi pi-box"></i>

          <span class="khmer-text">
            Category
          </span>
        </RouterLink>

        <RouterLink
          to="/admin/brand"
          class="menu-item"
          @click="onLinkClick"
        >
          <i class="pi pi-box"></i>

          <span class="khmer-text">
            Brand
          </span>
        </RouterLink>

        <RouterLink
          to="/admin/product"
          class="menu-item"
          @click="onLinkClick"
        >
          <i class="pi pi-box"></i>

          <span class="khmer-text">
            Product
          </span>
        </RouterLink>
        <RouterLink
          to="/admin/customer"
          class="menu-item"
          @click="onLinkClick"
        >
          <i class="pi pi-box"></i>

          <span class="khmer-text">
            Customer
          </span>
        </RouterLink>
        <RouterLink
          to="/admin/supplier"
          class="menu-item"
          @click="onLinkClick"
        >
          <i class="pi pi-box"></i>

          <span class="khmer-text">
            Supplier
          </span>
        </RouterLink>

      </nav>
      <div class="sidebar-footer">

        <RouterLink
          to="/"
          class="menu-item"
          @click="logout"
        >
          <i class="pi pi-sign-out"></i>

          <span>
            Logout
          </span>
        </RouterLink>

      </div>

    </aside>
    <main
      class="content"
      :class="{
        'content-sidebar-open':
          showSidebar &&
          !isMobile &&
          visible
      }"
    >

      <header
        v-if="showSidebar"
        class="top-bar"
      >

        <div class="top-left">

          <Button
            icon="pi pi-bars"
            class="menu-button"
            text
            @click="toggle"
          />

          <span class="page-title">
            {{ pageTitle }}
          </span>

        </div>
      </header>

      <section class="page-content">
        <router-view />
      </section>
    </main>
  </div>
</template>

<script setup>

import {
  ref,
  computed,
  onMounted,
  onUnmounted,
  watch
} from 'vue'

import {
  useRoute,
  useRouter
} from 'vue-router'

import Button from 'primevue/button'

const route = useRoute()
const router = useRouter()
const isLoggedIn = ref(false)
const userRole = ref('')
const isMobile = ref(
  window.innerWidth < 768
)

const visible = ref(
  window.innerWidth >= 768
)

// const showSidebar = computed(() => {
//   return !route.meta.hideSidebar
// })

const showSidebar = computed(() => {
  return isLoggedIn.value && !route.meta.hideSidebar
})

const pageTitle = computed(() => {
  return route.meta.title || ''
})

const checkLogin = () => {
  const user = localStorage.getItem('user')
  isLoggedIn.value = !!user
}

const getUserRole = () => {
  const user = localStorage.getItem('user')
  if (!user) {
    userRole.value = ''
    return
  }
  try {
    const userData = JSON.parse(user)
    userRole.value =
      userData.role_name || ''
  } catch (error) {
    console.error(
      'Invalid user data:',
      error
    )
    userRole.value = ''
  }
}

const handleResize = () => {

  const mobile =
    window.innerWidth < 768
  if (mobile !== isMobile.value) {
    isMobile.value = mobile
    if (mobile) {
      visible.value = false
    } else {
      visible.value = true
    }
  }
}

const toggle = () => {
  visible.value =
    !visible.value
}

const closeSidebar = () => {
  visible.value = false
}
const onLinkClick = () => {
  if (isMobile.value) {
    visible.value = false
  }
}

const login = () => {
  router.push('/login')
}

const logout = () => {
  localStorage.removeItem('user')
  isLoggedIn.value = false
  userRole.value = ''
  router.push('/login')
}

const handleStorage = () => {
  checkLogin()
  getUserRole()
}

watch(
  () => route.path,
  () => {
    if (isMobile.value) {
      visible.value = false
    }
    checkLogin()
    getUserRole()
  }
)
onMounted(() => {
  checkLogin()
  getUserRole()
  window.addEventListener(
    'resize',
    handleResize
  )
  window.addEventListener(
    'storage',
    handleStorage
  )
})

onUnmounted(() => {
  window.removeEventListener(
    'resize',
    handleResize
  )
  window.removeEventListener(
    'storage',
    handleStorage
  )
})
</script>

<style scoped>
.app-layout {
  width: 100%;
  height: 100vh;
  overflow: hidden;
  background: #ffffff;
}
.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  width: 260px;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background: #1f2937;
  color: #ffffff;
  z-index: 1000;
  overflow: hidden;
  white-space: nowrap;
  transition:
    width 0.3s ease;
}

.sidebar-open {
  width: 260px;
}

.sidebar-closed {
  width: 0;
}

.sidebar-header {
  width: 260px;
  min-width: 260px;
  height: 90px;
  display: flex;
  align-items: center;
  padding: 16px;
  box-sizing: border-box;
  flex-shrink: 0;
  border-bottom:
    1px solid #374151;
}

.logo {
  font-size: 28px;
  font-weight: 700;
  line-height: 1.2;
  color: #ffffff;
}

.sidebar-menu {
  width: 260px;
  min-width: 260px;
  flex: 1;
  padding: 12px;
  box-sizing: border-box;
  overflow-y: auto;
}

.menu-item {
  width: 100%;
  min-height: 48px;
  display: flex;
  align-items: center;
  box-sizing: border-box;
  padding: 12px 16px;
  margin-bottom: 4px;
  border-radius: 6px;
  color: #ffffff !important;
  text-decoration: none;
  font-size: 16px;
  transition:
    background 0.2s ease;
}

.menu-item i {
  width: 24px;
  margin-right: 12px;
  font-size: 18px;
  flex-shrink: 0;
  text-align: center;
}

.menu-item:hover {
  background: #374151;
  color: #ffffff !important;
}

.menu-item.router-link-active {
  background: #374151;
}

.khmer-text {
  font-family:
    "Noto Sans Khmer",
    "Khmer OS",
    "Khmer OS System",
    Battambang,
    sans-serif !important;
  white-space: nowrap;
}

.sidebar-footer {
  width: 260px;
  min-width: 260px;
  flex-shrink: 0;
  padding: 12px;
  box-sizing: border-box;
  border-top:
    1px solid #374151;
}

.content {
  width: 100%;
  height: 100vh;
  margin-left: 0;
  overflow: hidden;
  transition:
    margin-left 0.3s ease,
    width 0.3s ease;
}

.content-sidebar-open {
  margin-left: 260px;
  width: calc(100% - 260px);
}

.top-bar {
  height: 64px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  box-sizing: border-box;
  background: #ffffff;
  border-bottom:
    1px solid #e5e7eb;
  box-shadow:
    0 1px 3px rgba(0, 0, 0, 0.08);
  position: relative;
  z-index: 100;
}

.top-left {
  display: flex;
  align-items: center;
  min-width: 0;
}

.top-right {
  display: flex;
  align-items: center;
}

.menu-button {
  width: 42px !important;
  height: 42px !important;
  color: #10b981 !important;
}

.menu-button:hover {
  background:
    #ecfdf5 !important;
}

.page-title {
  margin-left: 8px;
  font-size: 22px;
  font-weight: 600;
  color: #10b981;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.login-button {
  color: #10b981 !important;
}
.page-content {
  height: calc(100vh - 64px);
  width: 100%;
  overflow-y: auto;
  overflow-x: hidden;
  box-sizing: border-box; 
}

.sidebar-backdrop {
  position: fixed;
  inset: 0;
  background:
    rgba(0, 0, 0, 0.5);
  z-index: 999;
}

@media (max-width: 767px) {
  .sidebar {
    width: 260px;
    transform:
      translateX(-100%);
    transition:
      transform 0.3s ease;
  }

  .sidebar-open {
    width: 260px;
    transform:
      translateX(0);
  }

  .sidebar-closed {
    width: 260px;
    transform:
      translateX(-100%);
  }
  .content,
  .content-sidebar-open {
    width: 100%;
    margin-left: 0;
  }
  .top-bar {
    padding:
      0 12px;
  }
  .page-title {
    font-size: 20px;
  }
  .page-content {
    padding: 12px;
  }
}
@media (max-width: 480px) {
  .page-title {
    font-size: 18px;
  }
  .top-bar {
    padding:
      0 8px;
  }
  .page-content {
    padding: 10px;
  }
}
</style>
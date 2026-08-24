import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'CustomerPage',
    component: () => import('../CustomerScreen/customerScreen.vue'),
    meta: { hideSidebar: true }
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/auth/Login.vue'),
    meta: { hideSidebar: true }
  },
  {
    path: '/admin/dashboard',
    name: 'Dashboard',
    component: () => import('../views/Dashboard.vue')
  },
  {
    path: '/admin/category',
    name: 'Category',
    component: () => import('../views/Category/category.vue')
  },
  {
    path: '/admin/brand',
    name: 'Brand',
    component: () => import('../views/Brand/brand.vue')
  },
  {
    path: '/admin/product',
    name: 'Product',
    component: () => import('../views/Product/product.vue')
  },
  {
    path: '/admin/customer',
    name: 'Customer',
    component: () => import('../views/Customer/customer.vue')
  },
  {
    path: '/admin/supplier',
    name: 'Supplier',
    component: () => import('../views/Supplier/supplier.vue')
  },
  
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

router.beforeEach((to, from, next) => {
  const user = localStorage.getItem('user')

  const requiresAuth = to.path.startsWith('/admin')

  if (requiresAuth && !user) {
    next('/login')
    return
  }

  if (to.path === '/login' && user) {
    next('/admin/dashboard')
    return
  }

  next()
})
import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

export const useAppStore = defineStore('app', () => {
  // Estado reactivo
  const isLoading = ref(false);
  const notifications = ref([]);
  const sidebarCollapsed = ref(false);
  const currentUser = ref(null);
  const theme = ref('light');
  const language = ref('es');
  
  // Contadores y datos principales
  const residentesCount = ref(0);
  const personalCount = ref(0);
  const gastosComunesCount = ref(0);
  const pagosPendientesCount = ref(0);
  
  // Computed properties
  const isAuthenticated = computed(() => !!currentUser.value);
  const hasNotifications = computed(() => notifications.value.length > 0);
  const unreadNotificationsCount = computed(() => 
    notifications.value.filter(n => !n.read).length
  );
  
  // Actions
  const setLoading = (loading) => {
    isLoading.value = loading;
  };
  
  const addNotification = (notification) => {
    const newNotification = {
      id: Date.now(),
      timestamp: new Date(),
      read: false,
      ...notification
    };
    notifications.value.unshift(newNotification);
    
    // Auto-remove after 5 seconds for success/info notifications
    if (['success', 'info'].includes(notification.type)) {
      setTimeout(() => {
        removeNotification(newNotification.id);
      }, 5000);
    }
  };
  
  const removeNotification = (id) => {
    const index = notifications.value.findIndex(n => n.id === id);
    if (index > -1) {
      notifications.value.splice(index, 1);
    }
  };
  
  const markNotificationAsRead = (id) => {
    const notification = notifications.value.find(n => n.id === id);
    if (notification) {
      notification.read = true;
    }
  };
  
  const clearAllNotifications = () => {
    notifications.value = [];
  };
  
  const toggleSidebar = () => {
    sidebarCollapsed.value = !sidebarCollapsed.value;
  };
  
  const setCurrentUser = (user) => {
    currentUser.value = user;
  };
  
  const logout = () => {
    // Limpiar usuario actual
    currentUser.value = null;
    
    // Limpiar notificaciones
    notifications.value = [];
    
    // Limpiar datos del dashboard
    residentesCount.value = 0;
    personalCount.value = 0;
    gastosComunesCount.value = 0;
    pagosPendientesCount.value = 0;
    
    // Limpiar localStorage
    localStorage.removeItem('isAuthenticated');
    localStorage.removeItem('userEmail');
    localStorage.removeItem('rememberMe');
  };
  
  const setTheme = (newTheme) => {
    theme.value = newTheme;
    document.documentElement.setAttribute('data-theme', newTheme);
  };
  
  const setLanguage = (newLanguage) => {
    language.value = newLanguage;
  };
  
  // Dashboard data actions
  const updateDashboardData = (data) => {
    if (data.residentesCount !== undefined) residentesCount.value = data.residentesCount;
    if (data.personalCount !== undefined) personalCount.value = data.personalCount;
    if (data.gastosComunesCount !== undefined) gastosComunesCount.value = data.gastosComunesCount;
    if (data.pagosPendientesCount !== undefined) pagosPendientesCount.value = data.pagosPendientesCount;
  };
  
  const incrementResidentesCount = () => {
    residentesCount.value++;
  };
  
  const decrementResidentesCount = () => {
    if (residentesCount.value > 0) {
      residentesCount.value--;
    }
  };
  
  return {
    // State
    isLoading,
    notifications,
    sidebarCollapsed,
    currentUser,
    theme,
    language,
    residentesCount,
    personalCount,
    gastosComunesCount,
    pagosPendientesCount,
    
    // Computed
    isAuthenticated,
    hasNotifications,
    unreadNotificationsCount,
    
    // Actions
    setLoading,
    addNotification,
    removeNotification,
    markNotificationAsRead,
    clearAllNotifications,
    toggleSidebar,
    setCurrentUser,
    logout,
    setTheme,
    setLanguage,
    updateDashboardData,
    incrementResidentesCount,
    decrementResidentesCount
  };
}); 
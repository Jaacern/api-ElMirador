// Estado global de alertas
let alertState = {
  show: false,
  type: 'info',
  title: '',
  message: '',
  showConfirm: false,
  showCancel: false,
  confirmText: 'Aceptar',
  cancelText: 'Cancelar',
  autoClose: true,
  autoCloseDelay: 3000,
  resolve: null
};

// Función para mostrar alerta
function mostrarAlerta(mensaje, tipo = 'info', titulo = '', opciones = {}) {
  alertState = {
    show: true,
    type: tipo,
    title: titulo || getDefaultTitle(tipo),
    message: mensaje,
    showConfirm: opciones.showConfirm || false,
    showCancel: opciones.showCancel || false,
    confirmText: opciones.confirmText || 'Aceptar',
    cancelText: opciones.cancelText || 'Cancelar',
    autoClose: opciones.autoClose !== false,
    autoCloseDelay: opciones.autoCloseDelay || 3000,
    resolve: null
  };
  
  // Emitir evento para actualizar el componente
  window.dispatchEvent(new CustomEvent('alert-update', { detail: alertState }));
}

// Función para confirmación
function confirm(mensaje) {
  return new Promise((resolve) => {
    alertState = {
      show: true,
      type: 'warning',
      title: 'Confirmar',
      message: mensaje,
      showConfirm: true,
      showCancel: true,
      confirmText: 'Aceptar',
      cancelText: 'Cancelar',
      autoClose: false,
      autoCloseDelay: 3000,
      resolve: resolve
    };
    
    window.dispatchEvent(new CustomEvent('alert-update', { detail: alertState }));
  });
}

// Función para cerrar alerta
function cerrarAlerta() {
  alertState.show = false;
  window.dispatchEvent(new CustomEvent('alert-update', { detail: alertState }));
}

// Función para manejar confirmación
function onConfirmarAlerta() {
  if (alertState.resolve) {
    alertState.resolve(true);
    alertState.resolve = null;
  }
  cerrarAlerta();
}

// Función para manejar cancelación
function onCancelarAlerta() {
  if (alertState.resolve) {
    alertState.resolve(false);
    alertState.resolve = null;
  }
  cerrarAlerta();
}

// Obtener título por defecto
function getDefaultTitle(tipo) {
  const titulos = {
    success: 'Éxito',
    error: 'Error',
    warning: 'Advertencia',
    info: 'Información'
  };
  return titulos[tipo] || 'Información';
}

// Métodos específicos
function mostrarExito(mensaje, titulo = 'Éxito') {
  mostrarAlerta(mensaje, 'success', titulo);
}

function mostrarError(mensaje, titulo = 'Error') {
  mostrarAlerta(mensaje, 'error', titulo, { autoClose: false });
}

function mostrarAdvertencia(mensaje, titulo = 'Advertencia') {
  mostrarAlerta(mensaje, 'warning', titulo);
}

function mostrarInfo(mensaje, titulo = 'Información') {
  mostrarAlerta(mensaje, 'info', titulo);
}

// Plugin de Vue
export default {
  install(app) {
    // Agregar métodos globales
    app.config.globalProperties.$alert = {
      mostrarAlerta,
      mostrarExito,
      mostrarError,
      mostrarAdvertencia,
      mostrarInfo,
      confirm,
      cerrarAlerta,
      onConfirmarAlerta,
      onCancelarAlerta,
      getState: () => alertState
    };
    
    // También agregar al objeto global
    window.$alert = {
      mostrarAlerta,
      mostrarExito,
      mostrarError,
      mostrarAdvertencia,
      mostrarInfo,
      confirm,
      cerrarAlerta,
      onConfirmarAlerta,
      onCancelarAlerta,
      getState: () => alertState
    };
  }
}; 
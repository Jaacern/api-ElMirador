export default {
  data() {
    return {
      alertConfig: {
        show: false,
        type: 'info',
        title: '',
        message: '',
        showConfirm: false,
        showCancel: false,
        confirmText: 'Aceptar',
        cancelText: 'Cancelar',
        autoClose: true,
        autoCloseDelay: 3000
      }
    };
  },
  methods: {
    // Método principal para mostrar alertas
    mostrarAlerta(mensaje, tipo = 'info', titulo = '', opciones = {}) {
      this.alertConfig = {
        show: true,
        type: tipo,
        title: titulo || this.getDefaultTitle(tipo),
        message: mensaje,
        showConfirm: opciones.showConfirm || false,
        showCancel: opciones.showCancel || false,
        confirmText: opciones.confirmText || 'Aceptar',
        cancelText: opciones.cancelText || 'Cancelar',
        autoClose: opciones.autoClose !== false,
        autoCloseDelay: opciones.autoCloseDelay || 3000
      };
    },

    // Métodos específicos para cada tipo de alerta
    mostrarExito(mensaje, titulo = 'Éxito') {
      this.mostrarAlerta(mensaje, 'success', titulo);
    },

    mostrarError(mensaje, titulo = 'Error') {
      this.mostrarAlerta(mensaje, 'error', titulo, { autoClose: false });
    },

    mostrarAdvertencia(mensaje, titulo = 'Advertencia') {
      this.mostrarAlerta(mensaje, 'warning', titulo);
    },

    mostrarInfo(mensaje, titulo = 'Información') {
      this.mostrarAlerta(mensaje, 'info', titulo);
    },

    // Método para confirmaciones
    mostrarConfirmacion(mensaje, titulo = 'Confirmar', opciones = {}) {
      this.mostrarAlerta(mensaje, 'warning', titulo, {
        showConfirm: true,
        showCancel: true,
        confirmText: opciones.confirmText || 'Aceptar',
        cancelText: opciones.cancelText || 'Cancelar',
        autoClose: false
      });
    },

    // Método para cerrar alerta
    cerrarAlerta() {
      this.alertConfig.show = false;
    },

    // Método para manejar confirmación
    onConfirmarAlerta() {
      if (this._confirmResolve) {
        this._confirmResolve(true);
        this._confirmResolve = null;
      }
      this.cerrarAlerta();
    },

    // Método para manejar cancelación
    onCancelarAlerta() {
      if (this._confirmResolve) {
        this._confirmResolve(false);
        this._confirmResolve = null;
      }
      this.cerrarAlerta();
    },

    // Obtener título por defecto según el tipo
    getDefaultTitle(tipo) {
      const titulos = {
        success: 'Éxito',
        error: 'Error',
        warning: 'Advertencia',
        info: 'Información'
      };
      return titulos[tipo] || 'Información';
    },

    // Reemplazar alert() del navegador
    alert(mensaje) {
      this.mostrarInfo(mensaje, 'Aviso');
    },

    // Reemplazar confirm() del navegador
    confirm(mensaje) {
      return new Promise((resolve) => {
        // Mostrar la alerta de confirmación
        this.alertConfig = {
          show: true,
          type: 'warning',
          title: 'Confirmar',
          message: mensaje,
          showConfirm: true,
          showCancel: true,
          confirmText: 'Aceptar',
          cancelText: 'Cancelar',
          autoClose: false
        };
        
        // Guardar las funciones de resolución
        this._confirmResolve = resolve;
      });
    },

    // Reemplazar prompt() del navegador (versión simplificada)
    prompt(mensaje, valorPorDefecto = '') {
      this.mostrarInfo(`Función prompt no disponible. Mensaje: ${mensaje}`, 'Aviso');
      return Promise.resolve(valorPorDefecto);
    }
  },

  // Interceptar alertas del navegador
  mounted() {
    // Reemplazar alert() global
    if (typeof window !== 'undefined') {
      const originalAlert = window.alert;
      window.alert = (mensaje) => {
        this.mostrarInfo(mensaje, 'Aviso');
      };

      // Reemplazar confirm() global
      const originalConfirm = window.confirm;
      window.confirm = (mensaje) => {
        return this.confirm(mensaje);
      };

      // Guardar referencias originales para restaurar si es necesario
      this._originalAlert = originalAlert;
      this._originalConfirm = originalConfirm;
    }
  },

  beforeUnmount() {
    // Restaurar funciones originales si es necesario
    if (typeof window !== 'undefined' && this._originalAlert) {
      window.alert = this._originalAlert;
      window.confirm = this._originalConfirm;
    }
  }
}; 
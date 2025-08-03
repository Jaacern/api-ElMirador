<template>
  <div class="chatbot-container">
    <!-- Botón flotante del chatbot -->
    <div class="chatbot-toggle" @click="toggleChat" :class="{ 'active': isOpen }">
      <i v-if="!isOpen" class="bi bi-chat-dots"></i>
      <i v-else class="bi bi-x-lg"></i>
    </div>

    <!-- Ventana del chat -->
    <div class="chatbot-window" :class="{ 'open': isOpen }">
      <div class="chatbot-header">
        <div class="chatbot-avatar">
          <i class="bi bi-robot"></i>
        </div>
        <div class="chatbot-info">
          <h6 class="mb-0">Asistente HR</h6>
          <small class="text-muted">En línea</small>
        </div>
        <button class="chatbot-close" @click="toggleChat">
          <i class="bi bi-x"></i>
        </button>
      </div>

      <div class="chatbot-messages" ref="messagesContainer">
        <div v-for="(message, index) in messages" :key="index" 
             class="message" :class="message.type">
          <div class="message-content">
            <div class="message-avatar" v-if="message.type === 'bot'">
              <i class="bi bi-robot"></i>
            </div>
            <div class="message-bubble">
              <p>{{ message.text }}</p>
              <small class="message-time">{{ message.time }}</small>
            </div>
            <div class="message-avatar" v-if="message.type === 'user'">
              <i class="bi bi-person"></i>
            </div>
          </div>
        </div>
      </div>

      <div class="chatbot-input">
        <div class="input-group">
          <input 
            type="text" 
            class="form-control" 
            v-model="userInput" 
            @keyup.enter="sendMessage"
            placeholder="Escribe tu mensaje..."
            :disabled="isTyping"
          >
          <button class="btn btn-primary" @click="sendMessage" :disabled="!userInput.trim() || isTyping">
            <i class="bi bi-send"></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChatbotComponent',
  data() {
    return {
      isOpen: false,
      userInput: '',
      isTyping: false,
      messages: [
        {
          type: 'bot',
          text: '¡Hola! Soy tu asistente HR de El Mirador. ¿En qué puedo ayudarte hoy?',
          time: this.getCurrentTime()
        }
      ]
    };
  },
  methods: {
    toggleChat() {
      this.isOpen = !this.isOpen;
      if (this.isOpen) {
        this.$nextTick(() => {
          this.scrollToBottom();
        });
      }
    },

    sendMessage() {
      if (!this.userInput.trim() || this.isTyping) return;

      // Agregar mensaje del usuario
      this.messages.push({
        type: 'user',
        text: this.userInput,
        time: this.getCurrentTime()
      });

      const userMessage = this.userInput.toLowerCase();
      this.userInput = '';
      this.isTyping = true;

      this.$nextTick(() => {
        this.scrollToBottom();
      });

      // Simular respuesta del bot
      setTimeout(() => {
        this.generateResponse(userMessage);
        this.isTyping = false;
        this.$nextTick(() => {
          this.scrollToBottom();
        });
      }, 1000);
    },

    generateResponse(userMessage) {
      let response = '';

      if (userMessage.includes('hola') || userMessage.includes('buenos días') || userMessage.includes('buenas')) {
        response = '¡Hola! ¿Cómo puedo ayudarte con la gestión del edificio El Mirador?';
      } else if (userMessage.includes('residente') || userMessage.includes('residentes')) {
        response = 'Para gestionar residentes, puedes ir a "Gestión Residentes" en el menú lateral. Allí podrás agregar, editar y ver la información de todos los residentes del edificio.';
      } else if (userMessage.includes('personal') || userMessage.includes('empleado')) {
        response = 'La gestión del personal se encuentra en "Gestión Personal". Puedes administrar empleados, cargos y estados del personal del edificio.';
      } else if (userMessage.includes('gasto') || userMessage.includes('gastos')) {
        response = 'Los gastos comunes se gestionan en "Gastos Comunes". Puedes registrar nuevos gastos, ver el estado de pagos y generar reportes financieros.';
      } else if (userMessage.includes('estadística') || userMessage.includes('estadísticas')) {
        response = 'En la sección "Estadísticas" encontrarás gráficos y análisis detallados sobre residentes, gastos, personal y el estado general del edificio.';
      } else if (userMessage.includes('reporte') || userMessage.includes('reportes')) {
        response = 'Los reportes personalizados están en "Reportes". Puedes generar reportes de residentes, gastos, personal y exportarlos en diferentes formatos.';
      } else if (userMessage.includes('herramienta') || userMessage.includes('herramientas')) {
        response = 'En "Herramientas" encontrarás calculadoras, generadores de reportes, backup del sistema y configuraciones avanzadas.';
      } else if (userMessage.includes('ayuda') || userMessage.includes('soporte')) {
        response = 'Para soporte técnico, puedes usar las herramientas del sistema o contactar al administrador. ¿Hay algo específico en lo que necesites ayuda?';
      } else if (userMessage.includes('gracias') || userMessage.includes('thanks')) {
        response = '¡De nada! Estoy aquí para ayudarte. Si tienes más preguntas, no dudes en preguntarme.';
      } else {
        response = 'Entiendo tu consulta. Te recomiendo revisar las diferentes secciones del sistema según lo que necesites: Gestión de Residentes, Personal, Gastos Comunes, Estadísticas o Reportes. ¿En qué área específica necesitas ayuda?';
      }

      this.messages.push({
        type: 'bot',
        text: response,
        time: this.getCurrentTime()
      });
    },

    getCurrentTime() {
      const now = new Date();
      return now.toLocaleTimeString('es-ES', { 
        hour: '2-digit', 
        minute: '2-digit' 
      });
    },

    scrollToBottom() {
      if (this.$refs.messagesContainer) {
        this.$refs.messagesContainer.scrollTop = this.$refs.messagesContainer.scrollHeight;
      }
    }
  }
};
</script>

<style scoped>
.chatbot-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 1000;
}

.chatbot-toggle {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: var(--shadow-lg);
  transition: all 0.3s ease;
  font-size: 1.5rem;
}

.chatbot-toggle:hover {
  transform: scale(1.1);
  box-shadow: 0 8px 25px rgba(37, 99, 235, 0.3);
}

.chatbot-toggle.active {
  background: linear-gradient(135deg, var(--danger-color), #dc2626);
}

.chatbot-window {
  position: absolute;
  bottom: 80px;
  right: 0;
  width: 350px;
  height: 500px;
  background: white;
  border-radius: 15px;
  box-shadow: var(--shadow-lg);
  display: flex;
  flex-direction: column;
  opacity: 0;
  visibility: hidden;
  transform: translateY(20px) scale(0.9);
  transition: all 0.3s ease;
}

.chatbot-window.open {
  opacity: 1;
  visibility: visible;
  transform: translateY(0) scale(1);
}

.chatbot-header {
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  color: white;
  padding: 15px;
  border-radius: 15px 15px 0 0;
  display: flex;
  align-items: center;
  gap: 10px;
}

.chatbot-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
}

.chatbot-info {
  flex: 1;
}

.chatbot-info h6 {
  margin: 0;
  font-weight: 600;
}

.chatbot-info small {
  opacity: 0.8;
}

.chatbot-close {
  background: none;
  border: none;
  color: white;
  font-size: 1.2rem;
  cursor: pointer;
  padding: 5px;
  border-radius: 50%;
  transition: all 0.2s ease;
}

.chatbot-close:hover {
  background: rgba(255, 255, 255, 0.2);
}

.chatbot-messages {
  flex: 1;
  padding: 15px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.message {
  display: flex;
  flex-direction: column;
}

.message-content {
  display: flex;
  align-items: flex-end;
  gap: 8px;
}

.message.user .message-content {
  flex-direction: row-reverse;
}

.message-avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9rem;
  flex-shrink: 0;
}

.message.bot .message-avatar {
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  color: white;
}

.message.user .message-avatar {
  background: linear-gradient(135deg, var(--success-color), #059669);
  color: white;
}

.message-bubble {
  max-width: 80%;
  padding: 12px 16px;
  border-radius: 18px;
  position: relative;
}

.message.bot .message-bubble {
  background: #f1f5f9;
  color: var(--dark-color);
  border-bottom-left-radius: 5px;
}

.message.user .message-bubble {
  background: linear-gradient(135deg, var(--primary-color), var(--primary-dark));
  color: white;
  border-bottom-right-radius: 5px;
}

.message-bubble p {
  margin: 0;
  font-size: 0.9rem;
  line-height: 1.4;
}

.message-time {
  font-size: 0.7rem;
  opacity: 0.7;
  margin-top: 5px;
  display: block;
}

.chatbot-input {
  padding: 15px;
  border-top: 1px solid #e2e8f0;
}

.input-group {
  display: flex;
  gap: 8px;
}

.input-group .form-control {
  border-radius: 20px;
  border: 1px solid #e2e8f0;
  padding: 10px 15px;
  font-size: 0.9rem;
}

.input-group .form-control:focus {
  border-color: var(--primary-color);
  box-shadow: 0 0 0 0.2rem rgba(37, 99, 235, 0.25);
}

.input-group .btn {
  border-radius: 50%;
  width: 40px;
  height: 40px;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Scrollbar personalizada */
.chatbot-messages::-webkit-scrollbar {
  width: 6px;
}

.chatbot-messages::-webkit-scrollbar-track {
  background: #f1f5f9;
  border-radius: 3px;
}

.chatbot-messages::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 3px;
}

.chatbot-messages::-webkit-scrollbar-thumb:hover {
  background: #94a3b8;
}

/* Responsive */
@media (max-width: 768px) {
  .chatbot-window {
    width: 300px;
    height: 400px;
    bottom: 70px;
  }
  
  .chatbot-toggle {
    width: 50px;
    height: 50px;
    font-size: 1.3rem;
  }
}
</style> 
<template>
    <div class="container">
        <h1 class="text-center my-4">Gestión de Gastos Comunes</h1>
  
        <!-- Formulario para generar gasto común (sin cambios) -->
        <div class="card mb-4">
            <div class="card-header">
                <h3>Generar Gasto Común</h3>
            </div>
            <div class="card-body">
                <form @submit.prevent="generarGastoComun">
                    <div class="mb-3">
                        <label class="form-label">Mes</label>
                        <select v-model="gastoForm.mes" class="form-select">
                            <option v-for="mes in meses" :key="mes" :value="mes">{{ mes }}</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Año</label>
                        <input type="number" v-model="gastoForm.anio" class="form-control" />
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Valor</label>
                        <input type="number" v-model="gastoForm.valor" class="form-control" />
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Departamento</label>
                        <select v-model="gastoForm.nro_departamento" class="form-select">
                            <option v-for="residente in residentes" :key="residente._id" :value="residente.nro_departamento">
                                {{ residente.nro_departamento }} - {{ residente.Nombre }} {{ residente.ApePat }}
                            </option>
                        </select>
                    </div>
                    <button type="submit" class="btn btn-primary">Generar Gasto Común</button>
                </form>
            </div>
        </div>
  
        <!-- Filtros actualizados -->
        <div class="card mb-4">
            <div class="card-header">
                <h3>Lista de Gastos Comunes</h3>
            </div>
            <div class="card-body">
                <div class="row mb-3">
                    <!-- Filtro de departamento -->
                    <div class="col-md-4">
                        <label class="form-label">Departamento</label>
                        <select v-model="filtros.departamento" class="form-select" @change="aplicarFiltros">
                            <option value="">Todos los departamentos</option>
                            <option v-for="residente in residentes" :key="residente._id" :value="residente.nro_departamento">
                                {{ residente.nro_departamento }} - {{ residente.Nombre }} {{ residente.ApePat }}
                            </option>
                        </select>
                    </div>

                    <!-- Filtro de estado -->
                    <div class="col-md-2">
                        <label class="form-label">Estado</label>
                        <select v-model="filtros.estado" class="form-select" @change="aplicarFiltros">
                            <option value="">Todos</option>
                            <option value="pagado">Pagados</option>
                            <option value="pendiente">Pendientes</option>
                        </select>
                    </div>

                    <!-- Filtro de año -->
                    <div class="col-md-2">
                        <label class="form-label">Año</label>
                        <select v-model="filtros.anio" class="form-select" @change="aplicarFiltros">
                            <option value="">Todos</option>
                            <option v-for="anio in aniosDisponibles" :key="anio" :value="anio">{{ anio }}</option>
                        </select>
                    </div>

                    <!-- Filtro de mes -->
                    <div class="col-md-2">
                        <label class="form-label">Mes</label>
                        <select v-model="filtros.mes" class="form-select" @change="aplicarFiltros">
                            <option value="">Todos</option>
                            <option v-for="mes in meses" :key="mes" :value="mes">{{ mes }}</option>
                        </select>
                    </div>

                    <!-- Ordenamiento por valor -->
                    <div class="col-md-2">
                        <label class="form-label">Ordenar valor</label>
                        <select v-model="filtros.ordenValor" class="form-select" @change="aplicarFiltros">
                            <option value="">Sin orden</option>
                            <option value="asc">Menor a mayor</option>
                            <option value="desc">Mayor a menor</option>
                        </select>
                    </div>
                </div>
  
                <!-- Tabla de gastos filtrados -->
                <div v-if="gastosFiltrados.length">
                    <h4>{{ obtenerTituloFiltros }}</h4>
                    <table class="table">
                        <thead>
                            <tr>
                                <th>Mes</th>
                                <th>Año</th>
                                <th>Valor</th>
                                <th>Estado</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="gasto in gastosFiltrados" :key="gasto._id">
                                <td>{{ gasto.mes }}</td>
                                <td>{{ gasto.anio }}</td>
                                <td>${{ gasto.valor }}</td>
                                <td>{{ gasto.estado_pago ? 'Pagado' : 'Pendiente' }}</td>
                                <td>
                                    <button 
                                        v-if="!gasto.estado_pago"
                                        class="btn btn-success btn-sm"
                                        @click="pagarGasto(gasto._id)"
                                    >
                                        Pagar
                                    </button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div v-else class="alert alert-info">
                    No se encontraron gastos con los filtros seleccionados
                </div>
            </div>
        </div>
  
        <!-- Sección de gastos pendientes (sin cambios) -->
        <div class="card">
            <div class="card-header d-flex justify-content-between align-items-center">
                <h3>Lista de Gastos Comunes Pendientes</h3>
                <button class="btn btn-primary" @click="generarInformeJSON">
                    Generar Informe JSON
                </button>
            </div>
            <div class="card-body">
                <table class="table">
                    <thead>
                        <tr>
                            <th>Mes</th>
                            <th>Año</th>
                            <th>Valor</th>
                            <th>Departamento</th>
                            <th>Estado</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="gasto in gastosPendientes" :key="gasto._id">
                            <td>{{ gasto.mes }}</td>
                            <td>{{ gasto.anio }}</td>
                            <td>${{ gasto.valor }}</td>
                            <td>{{ gasto.nro_departamento }}</td>
                            <td>Pendiente</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            meses: [
                'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
            ],
            gastoForm: {
                mes: '',
                anio: new Date().getFullYear(),
                valor: '',
                nro_departamento: ''
            },
            residentes: [],
            gastos: [],
            gastosPendientes: [],
            gastosFiltrados: [],
            filtros: {
                departamento: '',
                estado: '',
                anio: '',
                mes: '',
                ordenValor: ''
            },
            aniosDisponibles: []
        };
    },

    computed: {
        obtenerTituloFiltros() {
            const partes = [];
            
            if (this.filtros.departamento) {
                partes.push(`Depto ${this.filtros.departamento}`);
            }
            if (this.filtros.estado) {
                partes.push(this.filtros.estado === 'pagado' ? 'pagados' : 'pendientes');
            }
            if (this.filtros.anio) {
                partes.push(`del año ${this.filtros.anio}`);
            }
            if (this.filtros.mes) {
                partes.push(`del mes ${this.filtros.mes}`);
            }
            
            return partes.length ? 'Gastos para ' + partes.join(', ') : 'Todos los gastos';
        }
    },

    mounted() {
        this.cargarResidentes();
        this.cargarGastos();
        this.cargarGastosPendientes();
        this.generarAniosDisponibles();
    },

    methods: {
        async cargarResidentes() {
            try {
                const response = await axios.get('http://localhost:5000/residentes');
                this.residentes = response.data;
            } catch (error) {
                console.error('Error al cargar residentes:', error);
            }
        },

        async cargarGastos() {
            try {
                const response = await axios.get('http://localhost:5000/gastos-comunes');
                this.gastos = response.data;
                this.aplicarFiltros();
            } catch (error) {
                console.error('Error al cargar gastos:', error);
            }
        },

        async cargarGastosPendientes() {
            try {
                const response = await axios.get('http://localhost:5000/gastos-comunes/pendientes');
                this.gastosPendientes = response.data;
            } catch (error) {
                console.error('Error al cargar gastos pendientes:', error);
            }
        },

        generarAniosDisponibles() {
            const anioActual = new Date().getFullYear();
            this.aniosDisponibles = Array.from(
                { length: 5 },
                (_, i) => anioActual - i
            );
        },

        aplicarFiltros() {
            let gastosFiltrados = [...this.gastos];

            // Filtro por departamento
            if (this.filtros.departamento) {
                gastosFiltrados = gastosFiltrados.filter(
                    gasto => gasto.nro_departamento === this.filtros.departamento
                );
            }

            // Filtro por estado
            if (this.filtros.estado) {
                const estaPagado = this.filtros.estado === 'pagado';
                gastosFiltrados = gastosFiltrados.filter(
                    gasto => gasto.estado_pago === estaPagado
                );
            }

            // Filtro por año
            if (this.filtros.anio) {
                gastosFiltrados = gastosFiltrados.filter(
                    gasto => gasto.anio === parseInt(this.filtros.anio)
                );
            }

            // Filtro por mes
            if (this.filtros.mes) {
                gastosFiltrados = gastosFiltrados.filter(
                    gasto => gasto.mes === this.filtros.mes
                );
            }

            // Ordenar por valor
            if (this.filtros.ordenValor) {
                gastosFiltrados.sort((a, b) => {
                    if (this.filtros.ordenValor === 'asc') {
                        return a.valor - b.valor;
                    } else {
                        return b.valor - a.valor;
                    }
                });
            }

            this.gastosFiltrados = gastosFiltrados;
        },

        async generarGastoComun() {
            try {
                await axios.post('http://localhost:5000/gastos-comunes', this.gastoForm);
                alert('Gasto común generado exitosamente');
                this.cargarGastos();
                this.cargarGastosPendientes();
                // Resetear formulario
                this.gastoForm = {
                    mes: '',
                    anio: new Date().getFullYear(),
                    valor: '',
                    nro_departamento: ''
                };
            } catch (error) {
                console.error('Error al generar gasto común:', error);
                alert('Error al generar gasto común');
            }
        },

        async pagarGasto(id) {
            try {
                await axios.put(`http://localhost:5000/gastos-comunes/${id}`, {
                    estado_pago: true
                });
                alert('Gasto marcado como pagado');
                this.cargarGastos();
                this.cargarGastosPendientes();
            } catch (error) {
                console.error('Error al pagar gasto:', error);
                alert('Error al actualizar el estado del pago');
            }
        },

        generarInformeJSON() {
            const jsonData = JSON.stringify(this.gastosPendientes, null, 2);
            const blob = new Blob([jsonData], { type: 'application/json' });
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'gastos-pendientes.json';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
        }
    }
};
</script>

<style scoped>
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.card {
    margin-bottom: 20px;
}

.table {
    margin-top: 20px;
}

h1, .text-center.my-4 {
    color: #ffffff;
}

h2, h3, h4, .card-header h3 {
    color: #333333;
    font-family: 'GaretBook', sans-serif;
}

.card-header {
    background-color: #f8f9fa;
}

.card-header h3 {
    color: #333333;
    margin-bottom: 0;
}
</style>
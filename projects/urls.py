from rest_framework import routers
from .api import UsuarioViewSet, RolesViewSet, TareaViewSet, SprintViewSet, ProyectoViewSet, EquipoTrabajoViewSet, UsuarioEquipoViewSet, ComentarioViewSet

router = routers.DefaultRouter()

router.register('api/usuario', UsuarioViewSet, 'usuario')
router.register('api/roles', RolesViewSet, 'roles')
router.register('api/tarea', TareaViewSet, 'tarea')
router.register('api/sprint', SprintViewSet, 'sprint')
router.register('api/proyecto', ProyectoViewSet, 'proyecto')
router.register('api/equipo', EquipoTrabajoViewSet, 'equipo')
router.register('api/usuarioequipo', UsuarioEquipoViewSet, 'usuarioequipo')
router.register('api/comentario', ComentarioViewSet, 'comentario')

urlpatterns = router.urls


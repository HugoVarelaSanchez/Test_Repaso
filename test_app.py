#
# Copyright (C) 2025 Hugo Varela Sanchez (HugoVarelaSanchez)
# 
# Este archivo es parte de Test_Repaso
# GitHub: https://github.com/HugoVarelaSanchez/Test_Repaso
# 
# Test_Repaso es software libre: puedes redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General GNU versión 3
# publicada por la Free Software Foundation.
# 
# Test_Repaso se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; sin siquiera la garantía implícita de
# COMERCIABILIDAD o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Consulta
# la Licencia Pública General GNU para más detalles.
# 
# Deberías haber recibido una copia de la Licencia Pública General GNU
# junto con Test_Repaso. Si no es así, consulta <https://www.gnu.org/licenses/>.
#
from logger_config import logger
from utils.main import main

try:
    logger.info('Iniciando Test APP')
    main()
except KeyboardInterrupt:
    logger.info('Programa cerrado por el usuario')
    print('\n\nGracias por usar Test APP!\nCerrando programa.')
except Exception as e:
    logger.error(f'Error inesperado: {e}', exc_info=True)
    print(f'Error inesperado {e}')
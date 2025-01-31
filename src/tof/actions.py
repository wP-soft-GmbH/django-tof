import subprocess
from pathlib import Path

from tof.management.commands.create_js_from_static_translation import Command

from . import _, get_language
from .views import ActionView


class GenerateTranslationJSONFileAction(ActionView):
    description = _('Generate translation JSON file for front')
    short_description = _('Generate translation JSON file for front')
    allow_empty = True
    finished_message = _('Success')

    def processing(self, *args, **kwargs):
        if Path(f'{Command.locale_dir}').exists():
            current_lang_file = Path(f'{Command.locale_dir}') / f'{get_language()}.json'
            if not current_lang_file.exists():
                open(current_lang_file, 'a').close()
            Command().handle()
            return super().processing(*args, **kwargs)
        return self.cancel(message=_("Can not create language files, the path {} is not exists").format(Command.locale_dir))


class VueI18NExtractAction(ActionView):
    description = _('Extract translation from front')
    short_description = _('Extract translation from front')
    allow_empty = True
    finished_message = _('Success')

    def processing(self, *args, **kwargs):
        result = subprocess.run('npm run vue-i18n-extract', shell=True, cwd='front_vue', capture_output=True)
        if result.returncode:
            return self.error(_('Error: {}').format(result.stderr.decode()))
        return super().processing(*args, **kwargs)

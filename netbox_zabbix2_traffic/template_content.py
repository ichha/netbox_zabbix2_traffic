from netbox.plugins import PluginTemplateExtension

class InterfaceTrafficExtension(PluginTemplateExtension):
    model = 'dcim.interface'

    def full_width_page(self):
        # Retrieve the interface object being rendered in NetBox
        interface = self.context.get('object')
        if not interface or not interface.device:
            return ""

        # Render the custom traffic template, passing device and interface identifiers
        return self.render('netbox_zabbix2_traffic/inc/interface_traffic.html', extra_context={
            'device_name': interface.device.name,
            'interface_name': interface.name,
        })

template_extensions = [InterfaceTrafficExtension]

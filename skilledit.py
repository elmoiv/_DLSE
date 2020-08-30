class Editor:
    def __init__(self, xml_path):
        self.xml_path = xml_path
        self.xml_data = ''
        self.props = {}

    def load(self):
        # Get copy of original raw data
        with open(self.xml_path, 'r') as xml:
            self.xml_data = xml.read()
        
        with open(self.xml_path, 'r') as xml:
            for line in xml.readlines():
                # Get only important props
                line = line.strip().replace('\t', '')
                try:
                    # Skip comments and repetitive props
                    if line[:5] == '<prop':
                        name = line.split('n="')[-1].split('"')[0]
                        value = line.split('v="')[-1].split('"')[0]
                        # Store 2 instances of value to replace when update
                        value = [int, float]['.' in value](value)
                        self.props[name] = [value] * 2
                except:
                    pass

    def edit_prop(self, key, new_val):
        # Use type of old value as function to
        # force new value to be of same type
        t = type(self.props[key][1])
        if t is int and '.' in str(new_val):
            t = float
        self.props[key][0] = t(new_val)

    def update(self):
        for key in self.props:
            new_prop = f'<prop n="{key}" v="{self.props[key][0]}"/>'
            old_prop = f'<prop n="{key}" v="{self.props[key][1]}"/>'
            self.xml_data = self.xml_data.replace(
                                        old_prop,
                                        new_prop
                                        )
        
        with open(self.xml_path, 'w') as xml:
            xml.write(self.xml_data)
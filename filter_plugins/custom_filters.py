import ast

class FilterModule(object):
    def filters(self):
        return {
            'map_dict_list': self.map_dict_list,
            'filter_dict': self.filter_dict,
            'interface_format': self.interface_format
        }

    def map_dict_list(self, dict_list, mappings):
        if not isinstance(dict_list, list) or not isinstance(mappings, dict):
            raise Exception
        result = []
        for src_dict in dict_list:
            dst_dict = {}
            for src, dst in mappings.items():
                if src in src_dict.keys():
                    dst_dict[dst] = src_dict[src]
                else:
                    raise Exception
            result.append(dst_dict)
        return result

    def filter_dict(self, param, keys):
        if isinstance(param, dict):
            return self._filter_dict(param, keys)
        if isinstance(param, list):
            result = []
            for item in param:
                result.append(self._filter_dict(item, keys))
            return result
        raise Exception

    def interface_format(self, param, key, prefix='', suffix=''):
        if isinstance(param, list):
            result = []
            for item in param:
                if key in item.keys():
                    item[key] = prefix + str(item[key]) + suffix
                    result.append(item)
                else:
                    raise Exception
            return result
        if isinstance(param, dict):
            param[key] = prefix + str(param[key]) + suffix
            return param
        raise Exception

    @staticmethod
    def _filter_dict(param, keys):
        result = {}
        for key in keys:
            if key in param.keys():
                result[key] = param[key]
        return result

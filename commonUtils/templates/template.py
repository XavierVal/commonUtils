# -*- coding: utf-8 -*-

__author__ = 'x'

payload_template = """{
        "contextElements": [
            {
                "type": "{{ent_type}}",
                "isPattern": "{{ent_pattern}}",
                "id": "{{ent_id}}",
                "attributes": {{ent_attributes}}
            }],
        "updateAction": "{{action_mode}}"
    }"""

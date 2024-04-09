import random
import string

def mask_data(data, chars_to_mask=4):
    mask_char = "X"
    if len(data) <= chars_to_mask:
        return mask_char * len(data)
    else:
        masked_chars = data[:-chars_to_mask]
        for _ in range(chars_to_mask):
            masked_chars += mask_char
        return masked_chars

# Example usage:
sensitive_data = "1234-5678-9012-3456"
masked_data = mask_data(sensitive_data)
print("Masked Data:", masked_data)

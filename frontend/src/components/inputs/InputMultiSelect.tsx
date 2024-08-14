import { EuiComboBox } from '@elastic/eui'

export default function InputMultiSelect({
  options,
  value,
  onChange,
  ...props
}: any) {
  const selected = (value ?? []).map(tgt=>{
    if (typeof tgt ==="string") {
      return options.find(x => x.value === tgt)
    }
    return tgt
  }).filter(x=> !!x)

  
  return (
    <EuiComboBox
      {...props}
      options={options}
      selectedOptions={selected}
      onChange={option => {
        onChange((option??[]).map(x=>x.value))
      }}
      isClearable={true}
    />
  )
}

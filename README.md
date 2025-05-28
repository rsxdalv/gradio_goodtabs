Restoration of Gradio 4.x tab functionality for usage in [TTS WebUI](https://github.com/rsxdalv/tts-webui).

# `gradio_goodtabs`
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.3%20-%20orange">  

Python library for easily interacting with trained machine learning models

## Installation

```bash
pip install gradio_goodtabs
```

## Usage

```python

import gradio as gr
from gradio_goodtabs import GoodTabs
from gradio_goodtab import GoodTab as Tab
# from gradio_goodtabs import GoodTab as Tab
# gr.Tab = Tab
gr.Tabs = GoodTabs

with gr.Blocks() as demo:
    with gr.Row():
        with GoodTabs():  
            with Tab("Tab 1 long long long long long long long long long"):
                gr.Textbox(value="foo", interactive=True)
            with Tab("Tab 1 long long long long long long long long long"):
                gr.Textbox(value="foo", interactive=True)
            with Tab("Tab 1 long long long long long long long long long"):
                gr.Textbox(value="foo", interactive=True)
            with Tab("Tab 1 long long long long long long long long long"):
                gr.Textbox(value="foo", interactive=True)
            with Tab("Tab 1 long long long long long long long long long"):
                gr.Textbox(value="foo", interactive=True)
            with Tab("Tab 1 long long long long long long long long long"):
                gr.Textbox(value="foo", interactive=True)
            with Tab("Tab 1 long long long long long long long long long"):
                gr.Textbox(value="foo", interactive=True)
            with Tab("Tab 1 long long long long long long long long long"):
                gr.Textbox(value="foo", interactive=True)
            with Tab("Tab 1 long long long long long long long long long"):
                gr.Textbox(value="foo", interactive=True)
            with Tab("Tab 1 long long long long long long long long long"):
                gr.Textbox(value="foo", interactive=True)
            with Tab("Tab 1 long long long long long long long long long"):
                gr.Textbox(value="foo", interactive=True)
            with Tab("Tab 1 long long long long long long long long long"):
                gr.Textbox(value="foo", interactive=True)
            # with gr.Tab("Tab 1 long long long long long long long long long"):
            #     gr.Textbox(value="foo", interactive=True)
            # with gr.Tab("Tab 1 long long long long long long long long long"):
            #     gr.Textbox(value="foo", interactive=True)
            # with gr.Tab("Tab 1 long long long long long long long long long"):
            #     gr.Textbox(value="foo", interactive=True)
            # with gr.Tab("Tab 1 long long long long long long long long long"):
            #     gr.Textbox(value="foo", interactive=True)
            # with gr.Tab("Tab 1 long long long long long long long long long"):
            #     gr.Textbox(value="foo", interactive=True)
            # with gr.Tab("Tab 1 long long long long long long long long long"):
            #     gr.Textbox(value="foo", interactive=True)
            # with gr.Tab("Tab 2"):
            #     gr.Number(value=10, interactive=True)


if __name__ == "__main__":
    demo.launch()

```

## `GoodTab`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The visual label for the tab</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, Tab will be hidden.</td>
</tr>

<tr>
<td align="left"><code>interactive</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, Tab will not be clickable.</td>
</tr>

<tr>
<td align="left"><code>id</code></td>
<td align="left" style="width: 25%;">

```python
int | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional identifier for the tab, required if you wish to control the selected tab from a predict function.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string that is assigned as the id of the <div> containing the contents of the Tab layout. The same string followed by "-button" is attached to the Tab button. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string or list of strings that are assigned as the class of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, this layout will not be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `select` | Event listener for when the user selects or deselects the GoodTab. Uses event data gradio.SelectData to carry `value` referring to the label of the GoodTab, and `selected` to refer to state of the GoodTab. See EventData documentation on how to use this event data |




## `GoodTabs`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>selected</code></td>
<td align="left" style="width: 25%;">

```python
int | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The currently selected tab. Must correspond to an id passed to the one of the child TabItems. Defaults to the first TabItem.</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, GoodTabs will be hidden.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string or list of strings that are assigned as the class of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, this layout will not be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `change` | Triggered when the value of the GoodTabs changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `select` | Event listener for when the user selects or deselects the GoodTabs. Uses event data gradio.SelectData to carry `value` referring to the label of the GoodTabs, and `selected` to refer to state of the GoodTabs. See EventData documentation on how to use this event data |



